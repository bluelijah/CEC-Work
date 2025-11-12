import pandas as pd
import os
from difflib import get_close_matches
from fuzzywuzzy import fuzz
import numpy c

def get_column_mappings(csv_path):
    """Read the CSV and create a mapping from descriptive headers to column names using fuzzy matching."""
    # Read first two rows to get both header types
    df_headers = pd.read_csv(csv_path, nrows=0)  # Get column names (Q1, Q2, etc.)
    df_descriptive = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)  # Get descriptive headers

    column_names = df_headers.columns.tolist()
    descriptive_names = df_descriptive.columns.tolist()

    # Create mapping dictionary
    mappings = {
        'first_name': None,
        'last_name': None,
        'year': None,
        'school': None,
        'collegecorps': None,
        'recurring': None,
        'transfer': None
    }

    # Keywords to search for in descriptive headers
    keywords = {
        'first_name': ['first name', 'firstname'],
        'last_name': ['last name', 'lastname'],
        'year': ['academic year', 'year', 'class year'],
        'school': ['school', 'major housed'],
        'collegecorps': ['college corps', 'collegecorps'],
        'recurring': ['reoccurring', 'recurring', 'returning volunteer'],
        'transfer': ['transfer student', 'transfer']
    }

    # For each mapping we need, find the best match in descriptive headers
    for key, search_terms in keywords.items():
        best_score = 0
        best_col = None

        for i, desc in enumerate(descriptive_names):
            desc_lower = str(desc).lower()

            for term in search_terms:
                # Use fuzzy matching
                score = fuzz.partial_ratio(term, desc_lower)

                # Exact substring match gets bonus
                if term in desc_lower:
                    score += 20

                if score > best_score and score > 70:  # Threshold
                    best_score = score
                    best_col = column_names[i] if i < len(column_names) else None

        mappings[key] = best_col

    return mappings

def find_matching_csv(event_name, csv_folder):
    """Find a CSV file that matches the event name using fuzzy matching."""
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    if not csv_files:
        return None

    # Remove .csv extension for matching
    csv_names = [f[:-4] for f in csv_files]

    # Try exact match first (case-insensitive)
    for i, name in enumerate(csv_names):
        if event_name.lower() in name.lower() or name.lower() in event_name.lower():
            return os.path.join(csv_folder, csv_files[i])

    # Use fuzzy matching
    matches = get_close_matches(event_name.lower(), [n.lower() for n in csv_names], n=1, cutoff=0.3)

    if matches:
        # Find the original filename
        for i, name in enumerate(csv_names):
            if name.lower() == matches[0]:
                return os.path.join(csv_folder, csv_files[i])

    return None

def analyze_year(df, year_column):
    """Analyze student years from the CSV."""
    if not year_column or year_column not in df.columns:
        return None

    # Map values to year names
    year_mapping = {
        1: 'First Year',
        2: 'Second Year',
        3: 'Third Year',
        4: 'Fourth Year',
        5: 'Fifth Year+'
    }

    year_counts = {}
    for value in df[year_column].dropna():
        try:
            year_num = int(float(value))
            year_name = year_mapping.get(year_num, 'Other')
            year_counts[year_name] = year_counts.get(year_name, 0) + 1
        except (ValueError, TypeError):
            continue

    return year_counts if year_counts else None

def analyze_school(df, school_column):
    """Analyze schools from the CSV."""
    if not school_column or school_column not in df.columns:
        return None

    # Mapping: 1=Engineering, 2=Natural Sciences, 3=SSHA, 4=Undeclared
    school_mapping = {
        1: 'Engineering',
        2: 'Natural Sciences',
        3: 'Social Sciences, Humanities & Arts',
        4: 'Undeclared'
    }

    school_counts = {}
    for value in df[school_column].dropna():
        try:
            school_num = int(float(value))
            school_name = school_mapping.get(school_num)
            if school_name:
                school_counts[school_name] = school_counts.get(school_name, 0) + 1
        except (ValueError, TypeError):
            continue

    return school_counts if school_counts else None

def analyze_transfers(df, transfer_column):
    """Count transfer students."""
    if not transfer_column or transfer_column not in df.columns:
        return None

    # Mapping: 1=Yes (is transfer), 2=No (not transfer)
    transfer_count = 0
    for value in df[transfer_column].dropna():
        try:
            transfer_num = int(float(value))
            if transfer_num == 1:
                transfer_count += 1
        except (ValueError, TypeError):
            continue

    return transfer_count

def analyze_recurring(df, recurring_column):
    """Count recurring volunteers."""
    if not recurring_column or recurring_column not in df.columns:
        return None

    # Mapping: 1=Yes (recurring), 2=No (not recurring)
    recurring_count = 0
    for value in df[recurring_column].dropna():
        try:
            recurring_num = int(float(value))
            if recurring_num == 1:
                recurring_count += 1
        except (ValueError, TypeError):
            continue

    return recurring_count

def analyze_collegecorps(df, collegecorps_column):
    """Count CollegeCorps members."""
    if not collegecorps_column or collegecorps_column not in df.columns:
        return None

    # Mapping: 1=Yes (is CollegeCorps), 2=No (not CollegeCorps)
    collegecorps_count = 0
    for value in df[collegecorps_column].dropna():
        try:
            collegecorps_num = int(float(value))
            if collegecorps_num == 1:
                collegecorps_count += 1
        except (ValueError, TypeError):
            continue

    return collegecorps_count

def filter_empty_responses(df):
    """Remove rows where all question fields (after UserLanguage) are empty/null."""
    # Find the UserLanguage column
    user_language_index = None

    for idx, col in enumerate(df.columns):
        if 'userlanguage' in col.lower():
            user_language_index = idx
            break

    # If we can't find UserLanguage column, return original dataframe
    if user_language_index is None:
        return df

    # Get all columns after UserLanguage (these are the actual survey questions)
    question_columns = df.columns[user_language_index + 1:]

    if len(question_columns) == 0:
        return df

    # Filter out rows where ALL question columns are empty
    def is_valid_response(row):
        for col in question_columns:
            value = row[col]
            # If ANY question column has data, it's a valid response
            if pd.notna(value) and str(value).strip() != '':
                return True
        # If ALL question columns are empty, it's invalid
        return False

    # Apply filter
    filtered_df = df[df.apply(is_valid_response, axis=1)]

    rows_removed = len(df) - len(filtered_df)
    if rows_removed > 0:
        print(f"Note: Removed {rows_removed} empty/incomplete response(s)\n")

    return filtered_df

def filter_duplicate_responses(df, first_name_col, last_name_col):
    """Remove duplicate responses based on first and last name."""
    # If we can't find name columns, return original dataframe
    if not first_name_col or not last_name_col:
        return df

    if first_name_col not in df.columns or last_name_col not in df.columns:
        return df

    # Create a combined name column for duplicate checking (case-insensitive)
    df_temp = df.copy()
    df_temp['_full_name_lower'] = (
        df_temp[first_name_col].astype(str).str.strip().str.lower() + ' ' +
        df_temp[last_name_col].astype(str).str.strip().str.lower()
    )

    # Count duplicates before filtering
    duplicates_count = df_temp.duplicated(subset=['_full_name_lower'], keep='first').sum()

    # Remove duplicates, keeping the first occurrence
    filtered_df = df_temp.drop_duplicates(subset=['_full_name_lower'], keep='first')

    # Drop the temporary column
    filtered_df = filtered_df.drop(columns=['_full_name_lower'])

    if duplicates_count > 0:
        print(f"Note: Removed {duplicates_count} duplicate response(s)\n")

    return filtered_df

def main():
    # Get event name from user
    event_name = input("Enter event name: ").strip()

    if not event_name:
        print("Error: Please enter an event name.")
        return

    # Define CSV folder path
    csv_folder = "/Users/eli/Desktop/Code/Work Related/CEC/File Reading/csvs"

    # Find matching CSV
    csv_path = find_matching_csv(event_name, csv_folder)

    if not csv_path:
        print(f"\nNo CSV found matching '{event_name}'")
        print("\nAvailable CSV files:")
        csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
        for f in csv_files:
            print(f"  - {f[:-4]}")
        return

    print(f"\nFound matching CSV: {os.path.basename(csv_path)}")
    print("\nMapping columns using fuzzy matching on descriptive headers...")

    # Get column mappings based on descriptive headers
    mappings = get_column_mappings(csv_path)

    print("Analyzing data...\n")

    # Read CSV (use first row as header which contains Q2, Q3, Q4, etc.)
    try:
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])
    except:
        df = pd.read_csv(csv_path)

    # Clean up unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Filter out empty responses
    df = filter_empty_responses(df)

    # Filter out duplicate responses
    df = filter_duplicate_responses(df, mappings['first_name'], mappings['last_name'])

    # Total responses (after filtering)
    total_responses = len(df)
    print("=" * 60)
    print(f"EVENT ANALYSIS: {os.path.basename(csv_path)[:-4]}")
    print("=" * 60)
    print(f"\nTotal Responses: {total_responses}")

    # Analyze year distribution
    print("\n--- YEAR DISTRIBUTION ---")
    year_counts = analyze_year(df, mappings['year'])
    if year_counts:
        for year, count in sorted(year_counts.items()):
            print(f"{year}: {count}")
    else:
        print("Year data not available in this CSV")

    # Analyze school distribution
    print("\n--- SCHOOL DISTRIBUTION ---")
    school_counts = analyze_school(df, mappings['school'])
    if school_counts:
        for school, count in sorted(school_counts.items()):
            print(f"{school}: {count}")
    else:
        print("School data not available in this CSV")

    # Analyze transfers
    print("\n--- TRANSFER STUDENTS ---")
    transfer_count = analyze_transfers(df, mappings['transfer'])
    if transfer_count is not None:
        print(f"Transfer Students: {transfer_count}")
    else:
        print("Transfer data not available in this CSV")

    # Analyze recurring volunteers
    print("\n--- RECURRING VOLUNTEERS ---")
    recurring_count = analyze_recurring(df, mappings['recurring'])
    if recurring_count is not None:
        print(f"Recurring Volunteers: {recurring_count}")
    else:
        print("Recurring volunteer data not available in this CSV")

    # Analyze CollegeCorps
    print("\n--- COLLEGECORPS MEMBERS ---")
    collegecorps_count = analyze_collegecorps(df, mappings['collegecorps'])
    if collegecorps_count is not None:
        print(f"CollegeCorps Members: {collegecorps_count}")
    else:
        print("CollegeCorps data not available in this CSV")

    print("\n" + "=" * 60)
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()

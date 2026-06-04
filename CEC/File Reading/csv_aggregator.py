#To add a new metric to the CSV aggregator, follow this pattern: First, create an extraction function (e.g., extract_[metric]_data(csv_path))
#  that reads the CSV's three header rows - row 1 contains column codes (Q1, Q2, etc.), row 2 contains descriptive headers (the actual
#  questions), and row 3 contains metadata that should be skipped. Use find_column_by_keywords(descriptive_headers, column_codes, keywords) with
#  relevant keywords to fuzzy match against the descriptive headers and return the matching column code. For binary metrics (1=yes, 2=no),
#  iterate through the column values and count occurrences where value equals 1. For categorical metrics with multiple values (like school or
#  year), create a mapping dictionary and count occurrences of each category. The extraction function should return either a count (for binary
#  metrics), a dictionary of counts (for categorical metrics), or None if the column isn't found. Next, call your extraction function in main()
#  after the existing extraction calls. Finally, add a display section at the end of main() following the existing pattern with a header like
#  print("\n--- YOUR METRIC NAME ---") and appropriate conditional logic to handle cases where data isn't available. Always include descriptive
#  print statements showing which column was matched (e.g., print(f"  Found [metric] column '{column_code}': \"{desc_name}\"")). The fuzzy
#  matching system is flexible and will handle variations in question phrasing, typos (like "reoccurring" vs "recurring"), and different column
#  positions across CSV files.


import pandas as pd
import os
from fuzzywuzzy import fuzz
from collections import defaultdict

def find_column_by_keywords(descriptive_headers, column_codes, keywords, threshold=60):
    """
    Find a column that contains multiple keywords using fuzzy matching.

    Args:
        descriptive_headers: List of descriptive column names (row 2 of CSV)
        column_codes: List of column codes (row 1 of CSV, e.g., Q1, Q2, Q3)
        keywords: List of keywords to look for (e.g., ['school', 'major', 'department'])
        threshold: Minimum fuzzy match score (0-100)

    Returns:
        The column code (e.g., 'Q3') of the best matching column, or None
    """
    best_score = 0
    best_column_index = None

    for i, desc in enumerate(descriptive_headers):
        desc_lower = str(desc).lower()

        # Calculate a combined score based on how many keywords match
        total_score = 0
        matches = 0

        for keyword in keywords:
            # Use partial ratio for fuzzy matching
            score = fuzz.partial_ratio(keyword.lower(), desc_lower)

            # Bonus for exact substring match
            if keyword.lower() in desc_lower:
                score += 30
                matches += 1

            total_score += score

        # Average score across all keywords, with bonus for multiple matches
        avg_score = total_score / len(keywords)
        if matches > 1:
            avg_score += 20  # Bonus if multiple keywords found in same column

        if avg_score > best_score and avg_score >= threshold:
            best_score = avg_score
            best_column_index = i

    if best_column_index is not None and best_column_index < len(column_codes):
        return column_codes[best_column_index]

    return None


def extract_school_data(csv_path):
    """
    Extract school/department data from a CSV file using fuzzy matching.

    Returns:
        Dictionary with counts of each school, or None if column not found
    """
    try:
        # Read the first row (column codes like Q1, Q2, Q3)
        df_codes = pd.read_csv(csv_path, nrows=0)
        column_codes = df_codes.columns.tolist()

        # Read the second row (descriptive headers)
        df_desc = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)
        descriptive_headers = df_desc.columns.tolist()

        # Read the actual data (skip first 3 rows: codes, descriptions, metadata)
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])

        # Clean unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Find the school/department column using fuzzy matching on descriptive headers
        # Looking for columns that mention school, major, and/or department
        school_keywords = ['school', 'major', 'housed']
        school_column = find_column_by_keywords(descriptive_headers, column_codes, school_keywords)

        if not school_column:
            return None

        # Find the descriptive name for display
        if school_column in column_codes:
            idx = column_codes.index(school_column)
            if idx < len(descriptive_headers):
                desc_name = descriptive_headers[idx]
                print(f"  Found school column '{school_column}': \"{desc_name}\"")
            else:
                print(f"  Found school column: '{school_column}'")
        else:
            print(f"  Found school column: '{school_column}'")

        # School mapping (same as in event_analyzer.py)
        school_mapping = {
            1: 'Engineering',
            2: 'Natural Sciences',
            3: 'Social Sciences, Humanities & Arts',
            4: 'Undeclared'
        }

        # Count responses for each school
        school_counts = defaultdict(int)

        for value in df[school_column].dropna():
            try:
                school_num = int(float(value))
                school_name = school_mapping.get(school_num)
                if school_name:
                    school_counts[school_name] += 1
            except (ValueError, TypeError):
                # Handle non-numeric values if needed
                continue

        return dict(school_counts) if school_counts else None

    except Exception as e:
        print(f"  Error reading {os.path.basename(csv_path)}: {str(e)}")
        return None


def extract_year_data(csv_path):
    """
    Extract academic year data from a CSV file using fuzzy matching.

    Returns:
        Dictionary with counts of each year, or None if column not found
    """
    try:
        # Read the first row (column codes like Q1, Q2, Q3)
        df_codes = pd.read_csv(csv_path, nrows=0)
        column_codes = df_codes.columns.tolist()

        # Read the second row (descriptive headers)
        df_desc = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)
        descriptive_headers = df_desc.columns.tolist()

        # Read the actual data (skip first 3 rows: codes, descriptions, metadata)
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])

        # Clean unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Find the year column using fuzzy matching on descriptive headers
        # Looking for columns that mention year, academic, grade, class
        year_keywords = ['year', 'academic', 'grade', 'class']
        year_column = find_column_by_keywords(descriptive_headers, column_codes, year_keywords)

        if not year_column:
            return None

        # Find the descriptive name for display
        if year_column in column_codes:
            idx = column_codes.index(year_column)
            if idx < len(descriptive_headers):
                desc_name = descriptive_headers[idx]
                print(f"  Found year column '{year_column}': \"{desc_name}\"")
            else:
                print(f"  Found year column: '{year_column}'")
        else:
            print(f"  Found year column: '{year_column}'")

        # Year mapping
        year_mapping = {
            1: 'Freshman',
            2: 'Sophomore',
            3: 'Junior',
            4: 'Senior',
            5: 'Other'
        }

        # Count responses for each year
        year_counts = defaultdict(int)

        for value in df[year_column].dropna():
            try:
                year_num = int(float(value))
                year_name = year_mapping.get(year_num)
                if year_name:
                    year_counts[year_name] += 1
            except (ValueError, TypeError):
                # Handle non-numeric values if needed
                continue

        return dict(year_counts) if year_counts else None

    except Exception as e:
        print(f"  Error reading year data from {os.path.basename(csv_path)}: {str(e)}")
        return None


def extract_transfer_data(csv_path):
    """
    Extract transfer student data from a CSV file using fuzzy matching.

    Returns:
        Count of transfer students (value = 1), or None if column not found
    """
    try:
        # Read the first row (column codes like Q1, Q2, Q3)
        df_codes = pd.read_csv(csv_path, nrows=0)
        column_codes = df_codes.columns.tolist()

        # Read the second row (descriptive headers)
        df_desc = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)
        descriptive_headers = df_desc.columns.tolist()

        # Read the actual data (skip first 3 rows: codes, descriptions, metadata)
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])

        # Clean unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Find the transfer column using fuzzy matching on descriptive headers
        # Looking for columns that mention transfer, student
        transfer_keywords = ['transfer', 'student']
        transfer_column = find_column_by_keywords(descriptive_headers, column_codes, transfer_keywords)

        if not transfer_column:
            return None

        # Find the descriptive name for display
        if transfer_column in column_codes:
            idx = column_codes.index(transfer_column)
            if idx < len(descriptive_headers):
                desc_name = descriptive_headers[idx]
                print(f"  Found transfer column '{transfer_column}': \"{desc_name}\"")
            else:
                print(f"  Found transfer column: '{transfer_column}'")
        else:
            print(f"  Found transfer column: '{transfer_column}'")

        # Count transfer students (value = 1 means yes)
        transfer_count = 0

        for value in df[transfer_column].dropna():
            try:
                transfer_num = int(float(value))
                if transfer_num == 1:
                    transfer_count += 1
            except (ValueError, TypeError):
                continue

        return transfer_count

    except Exception as e:
        print(f"  Error reading transfer data from {os.path.basename(csv_path)}: {str(e)}")
        return None


def extract_recurring_data(csv_path):
    """
    Extract recurring volunteer data from a CSV file using fuzzy matching.

    Returns:
        Count of recurring volunteers (value = 1), or None if column not found
    """
    try:
        # Read the first row (column codes like Q1, Q2, Q3)
        df_codes = pd.read_csv(csv_path, nrows=0)
        column_codes = df_codes.columns.tolist()

        # Read the second row (descriptive headers)
        df_desc = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)
        descriptive_headers = df_desc.columns.tolist()

        # Read the actual data (skip first 3 rows: codes, descriptions, metadata)
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])

        # Clean unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Find the recurring volunteer column using fuzzy matching on descriptive headers
        # Looking for columns that mention recurring, reoccurring, volunteer, returning
        recurring_keywords = ['recurring', 'reoccurring', 'volunteer', 'returning']
        recurring_column = find_column_by_keywords(descriptive_headers, column_codes, recurring_keywords)

        if not recurring_column:
            return None

        # Find the descriptive name for display
        if recurring_column in column_codes:
            idx = column_codes.index(recurring_column)
            if idx < len(descriptive_headers):
                desc_name = descriptive_headers[idx]
                print(f"  Found recurring column '{recurring_column}': \"{desc_name}\"")
            else:
                print(f"  Found recurring column: '{recurring_column}'")
        else:
            print(f"  Found recurring column: '{recurring_column}'")

        # Count recurring volunteers (value = 1 means yes)
        recurring_count = 0

        for value in df[recurring_column].dropna():
            try:
                recurring_num = int(float(value))
                if recurring_num == 1:
                    recurring_count += 1
            except (ValueError, TypeError):
                continue

        return recurring_count

    except Exception as e:
        print(f"  Error reading recurring data from {os.path.basename(csv_path)}: {str(e)}")
        return None


def extract_collegecorps_data(csv_path):
    """
    Extract CollegeCorps member data from a CSV file using fuzzy matching.

    Returns:
        Count of CollegeCorps members (value = 1), or None if column not found
    """
    try:
        # Read the first row (column codes like Q1, Q2, Q3)
        df_codes = pd.read_csv(csv_path, nrows=0)
        column_codes = df_codes.columns.tolist()

        # Read the second row (descriptive headers)
        df_desc = pd.read_csv(csv_path, skiprows=[0, 2], nrows=0)
        descriptive_headers = df_desc.columns.tolist()

        # Read the actual data (skip first 3 rows: codes, descriptions, metadata)
        df = pd.read_csv(csv_path, header=0, skiprows=[1, 2])

        # Clean unnamed columns
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Find the CollegeCorps column using fuzzy matching on descriptive headers
        # Looking for columns that mention college, corps, collegecorps
        collegecorps_keywords = ['college', 'corps', 'collegecorps']
        collegecorps_column = find_column_by_keywords(descriptive_headers, column_codes, collegecorps_keywords)

        if not collegecorps_column:
            return None

        # Find the descriptive name for display
        if collegecorps_column in column_codes:
            idx = column_codes.index(collegecorps_column)
            if idx < len(descriptive_headers):
                desc_name = descriptive_headers[idx]
                print(f"  Found CollegeCorps column '{collegecorps_column}': \"{desc_name}\"")
            else:
                print(f"  Found CollegeCorps column: '{collegecorps_column}'")
        else:
            print(f"  Found CollegeCorps column: '{collegecorps_column}'")

        # Count CollegeCorps members (value = 1 means yes)
        collegecorps_count = 0

        for value in df[collegecorps_column].dropna():
            try:
                collegecorps_num = int(float(value))
                if collegecorps_num == 1:
                    collegecorps_count += 1
            except (ValueError, TypeError):
                continue

        return collegecorps_count

    except Exception as e:
        print(f"  Error reading CollegeCorps data from {os.path.basename(csv_path)}: {str(e)}")
        return None


def find_matching_csv(event_name, csv_folder):
    """Find a CSV file that matches the event name using fuzzy matching."""
    from difflib import get_close_matches

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
    print()

    # Extract school data
    school_data = extract_school_data(csv_path)

    # Extract year data
    year_data = extract_year_data(csv_path)

    # Extract transfer data
    transfer_count = extract_transfer_data(csv_path)

    # Extract recurring volunteer data
    recurring_count = extract_recurring_data(csv_path)

    # Extract CollegeCorps data
    collegecorps_count = extract_collegecorps_data(csv_path)

    # Display results
    print()
    print("=" * 60)
    print(f"EVENT ANALYSIS: {os.path.basename(csv_path)[:-4]}")
    print("=" * 60)

    # Calculate total from whichever dataset is available
    total = 0
    if school_data:
        total = sum(school_data.values())
    elif year_data:
        total = sum(year_data.values())

    print(f"\nTotal Responses: {total}")

    # Display school distribution
    if school_data:
        print("\n--- SCHOOL DISTRIBUTION ---")
        school_order = [
            'Engineering',
            'Natural Sciences',
            'Social Sciences, Humanities & Arts',
            'Undeclared'
        ]

        for school in school_order:
            if school in school_data:
                count = school_data[school]
                print(f"{school}: {count}")
    else:
        print("\n--- SCHOOL DISTRIBUTION ---")
        print("School data not available in this CSV")

    # Display year distribution
    if year_data:
        print("\n--- YEAR DISTRIBUTION ---")
        year_order = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Other']

        for year in year_order:
            if year in year_data:
                count = year_data[year]
                print(f"{year}: {count}")
    else:
        print("\n--- YEAR DISTRIBUTION ---")
        print("Year data not available in this CSV")

    # Display transfer students
    print("\n--- TRANSFER STUDENTS ---")
    if transfer_count is not None:
        print(f"Transfer Students: {transfer_count}")
    else:
        print("Transfer data not available in this CSV")

    # Display recurring volunteers
    print("\n--- RECURRING VOLUNTEERS ---")
    if recurring_count is not None:
        print(f"Recurring Volunteers: {recurring_count}")
    else:
        print("Recurring volunteer data not available in this CSV")

    # Display CollegeCorps members
    print("\n--- COLLEGECORPS MEMBERS ---")
    if collegecorps_count is not None:
        print(f"CollegeCorps Members: {collegecorps_count}")
    else:
        print("CollegeCorps data not available in this CSV")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

import pandas as pd

# Load CSV, use second row (row index 1) as header, skip the Qualtrics metadata row
df = pd.read_csv("csvs/audiophoto.csv", header=1, skiprows=[2])

# Remove any "Unnamed" columns that Qualtrics sometimes adds
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Rename long Qualtrics columns for easier access
rename_map = {}
for col in df.columns:
    if "Full Name" in col and "Please respond" in col:
        rename_map[col] = "Full Name"
    elif "Email Address" in col and "Please respond" in col:
        rename_map[col] = "Email Address"
    elif "Phone Number" in col and "Please respond" in col:
        rename_map[col] = "Phone Number"
    elif "Street Address" in col and "Please respond" in col:
        rename_map[col] = "Street Address"
    elif "Date" in col and "Please respond" in col:
        rename_map[col] = "Date"
df.rename(columns=rename_map, inplace=True)

# Ask user for input
query = input("Enter student name or email: ").strip().lower()

# Search by Full Name or Email Address
results = df[
    df["Full Name"].astype(str).str.lower().str.contains(query) |
    df["Email Address"].astype(str).str.lower().str.contains(query)
]

if results.empty:
    print("No student found with that name or email.")
else:
    for _, row in results.iterrows():
        print("\n--- Student Record ---")
        for col, val in row.items():
            print(f"{col}: {val}")

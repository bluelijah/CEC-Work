import pandas as pd

# Load CSV, use second row (row index 1) as header
df = pd.read_csv("csvs/confidentiality.csv", header=1)

# Remove any "Unnamed" columns that Qualtrics sometimes adds
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Build a FullName column
df["FullName"] = (
    df["First Name"].astype(str).str.strip() + " " +
    df["Last Name"].astype(str).str.strip()
)

# Ask user for input
query = input("Enter student name or email: ").strip().lower()  # CHANGED: Updated prompt text

# Search FullName, First, Last, or Email
results = df[
    df["FullName"].str.lower().str.contains(query) |
    df["First Name"].str.lower().str.contains(query) |
    df["Last Name"].str.lower().str.contains(query) |
    df["UCM Email"].str.lower().str.contains(query)  # ADDED: Email search condition
]

if results.empty:
    print("No student found with that name or email.")  # CHANGED: Updated message
else:
    for _, row in results.iterrows():
        print("\n--- Student Record ---")
        for col, val in row.items():
            print(f"{col}: {val}")
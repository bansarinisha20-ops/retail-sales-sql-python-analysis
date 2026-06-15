import pandas as pd
# Load dataset
df = pd.read_csv("/Users/daneshkumar/Desktop/file organizer/online_retail_ll.csv")
print("Original Shape:", df.shape)
# Remove null Customer IDs
df = df[df['Customer ID'].notna()]
# Remove cancelled invoices
df = df[~df['Invoice'].astype(str).str.startswith('C')]
# Remove negative quantities
df = df[df['Quantity'] > 0]
# Create Revenue column
df['Revenue'] = df['Quantity'] * df['Price']
print("Cleaned Shape:", df.shape)
# Save cleaned dataset
df.to_csv("retail_cleaned.csv", index=False)
print("Cleaning Complete")
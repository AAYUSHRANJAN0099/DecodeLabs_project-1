import pandas as pd

df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("===== DATASET INFO =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("\nDuplicate Rows:", df.duplicated().sum())
print("Duplicate Order IDs:", df["OrderID"].duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print(
    "\nInvalid Dates:",
    df["Date"].isnull().sum()
)

df. to_excel(
    "Cleaned_Dataset.xlsx",
    index=False
)

print("\nDataset cleaned successfully!")
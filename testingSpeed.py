import pandas as pd
import time

data = [
    {"TRAN_DATE": "2024-06-01", "AMOUNT": 2000, "SENDER_NAME": "Alice", "SENDER_BANK": "A1", "BENEFICIARY_NAME": "Bob", "BENEFICIARY_BANK": "B1"},
    {"TRAN_DATE": "2024-06-02", "AMOUNT": 3000, "SENDER_NAME": "Charlie", "SENDER_BANK": "A2", "BENEFICIARY_NAME": "Bob", "BENEFICIARY_BANK": "B1"},
    {"TRAN_DATE": "2024-07-02", "AMOUNT": 3000, "SENDER_NAME": "Charlie", "SENDER_BANK": "A2", "BENEFICIARY_NAME": "Bob", "BENEFICIARY_BANK": "B1"},
    {"TRAN_DATE": "2024-07-12", "AMOUNT": 3000, "SENDER_NAME": "Charlie", "SENDER_BANK": "A2", "BENEFICIARY_NAME": "Bob", "BENEFICIARY_BANK": "B1"},
    {"TRAN_DATE": "2024-07-22", "AMOUNT": 3000, "SENDER_NAME": "Charlie", "SENDER_BANK": "A2", "BENEFICIARY_NAME": "Bob", "BENEFICIARY_BANK": "B1"}
]

data = [{"TRAN_NO": None, "SENDER_NAME": None, "SENDER_BANK": None, "SENDER_COUNTRY": None, "BENEFICIARY_NAME": None, "BENEFICIARY_BANK": None, "BENEFICIARY_COUNTRY": None, "TRAN_DATE": "16 October 2024", "DIRECTION": "CREDIT", "AMOUNT": 12345.0}, {"TRAN_NO": None, "SENDER_NAME": None, "SENDER_BANK": None, "SENDER_COUNTRY": None, "BENEFICIARY_NAME": None, "BENEFICIARY_BANK": None, "BENEFICIARY_COUNTRY": None, "TRAN_DATE": "18 October 2024", "DIRECTION": "CREDIT", "AMOUNT": 123.0}, {"TRAN_NO": None, "SENDER_NAME": None, "SENDER_BANK": None, "SENDER_COUNTRY": None, "BENEFICIARY_NAME": None, "BENEFICIARY_BANK": None, "BENEFICIARY_COUNTRY": None, "TRAN_DATE": "22 October 2024", "DIRECTION": "CREDIT", "AMOUNT": 123.0}]

start = time.time()


# Convert to DataFrame
df = pd.DataFrame(data)
df.fillna('unknown', inplace=True)

# Ensure date is datetime
df["TRAN_DATE"] = pd.to_datetime(df["TRAN_DATE"])

# Group by sender and beneficiary names (with banks)
group_cols = ["SENDER_NAME", "SENDER_BANK", "BENEFICIARY_NAME", "BENEFICIARY_BANK"]

# Aggregate: sum amount, min date, max date
aggDf = df.groupby(group_cols).agg(
    TOTAL_AMOUNT=("AMOUNT", "sum"),
    FIRST_TRAN_DATE=("TRAN_DATE", "min"),
    LAST_TRAN_DATE=("TRAN_DATE", "max")
).reset_index()

aggDf['FIRST_TRAN_DATE'] = aggDf['FIRST_TRAN_DATE'].dt.strftime('%Y-%m-%d')
aggDf['LAST_TRAN_DATE'] = aggDf['LAST_TRAN_DATE'].dt.strftime('%Y-%m-%d')

# Optional: convert to list of dicts
result = aggDf.to_dict(orient="records")

# Print or return result
print(result)


end = time.time()
print(end - start)
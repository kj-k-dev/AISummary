# data = [{"TRAN_NO": null, "SENDER_NAME": null, "SENDER_BANK": null, "SENDER_COUNTRY": null, "BENEFICIARY_NAME": null, "BENEFICIARY_BANK": null, "BENEFICIARY_COUNTRY": null, "TRAN_DATE": 20241016, "DIRECTION": "CREDIT", "AMOUNT": 12345.0}, {"TRAN_NO": null, "SENDER_NAME": null, "SENDER_BANK": null, "SENDER_COUNTRY": null, "BENEFICIARY_NAME": null, "BENEFICIARY_BANK": null, "BENEFICIARY_COUNTRY": null, "TRAN_DATE": 20241022, "DIRECTION": "CREDIT", "AMOUNT": 123.0}, {"TRAN_NO": null, "SENDER_NAME": null, "SENDER_BANK": null, "SENDER_COUNTRY": null, "BENEFICIARY_NAME": null, "BENEFICIARY_BANK": null, "BENEFICIARY_COUNTRY": null, "TRAN_DATE": 20241018, "DIRECTION": "CREDIT", "AMOUNT": 123.0}]

# import numpy as np

# # Extract sender, beneficiary, and amount
# senders = np.array([d["sender"] for d in data])
# beneficiaries = np.array([d["beneficiary"] for d in data])
# amounts = np.array([d["amount"] for d in data])

# # Combine sender and beneficiary as grouping key
# keys = np.char.add(senders, '||' + beneficiaries)

# # Find unique groups and inverse indices
# unique_keys, inverse = np.unique(keys, return_inverse=True)

# # Sum amounts for each group
# sums = np.zeros(len(unique_keys), dtype=int)
# np.add.at(sums, inverse, amounts)

# # Construct result list of dicts
# results = []
# for i, key in enumerate(unique_keys):
#     sender, beneficiary = key.split('||')
#     results.append({
#         "sender": sender,
#         "beneficiary": beneficiary,
#         "total_amount": sums[i]
#     })

# print(results)
# print(results[1]['total_amount'])

import numpy as np

# Sample data (with sender_bank and beneficiary_bank added)
data = [
    {"date": "2024-06-01", "amount": 2000, "sender": "Alice", "sender_bank": "BankX", "beneficiary": "Bob", "beneficiary_bank": "BankY"},
    {"date": "2024-06-02", "amount": 3000, "sender": "Charlie", "sender_bank": "BankA", "beneficiary": "Bob", "beneficiary_bank": "BankB"},
    {"date": "2024-07-02", "amount": 3000, "sender": "Charlie", "sender_bank": "BankA", "beneficiary": "Bob", "beneficiary_bank": "BankB"},
    {"date": "2024-07-12", "amount": 3000, "sender": "Charlie", "sender_bank": "BankA", "beneficiary": "Bob", "beneficiary_bank": "BankB"},
    {"date": "2024-07-22", "amount": 3000, "sender": "Charlie", "sender_bank": "BankA", "beneficiary": "Bob", "beneficiary_bank": "BankB"}
]

# Extract fields into numpy arrays
senders = np.array([d["sender"] for d in data])
sender_banks = np.array([d["sender_bank"] for d in data])
beneficiaries = np.array([d["beneficiary"] for d in data])
beneficiary_banks = np.array([d["beneficiary_bank"] for d in data])
amounts = np.array([d["amount"] for d in data])

# Create a unique key from all grouping fields
keys = np.char.add(senders, '|')
keys = np.char.add(keys, sender_banks)
keys = np.char.add(keys, '|')
keys = np.char.add(keys, beneficiaries)
keys = np.char.add(keys, '|')
keys = np.char.add(keys, beneficiary_banks)

# Group by keys
unique_keys, inverse = np.unique(keys, return_inverse=True)
sums = np.zeros(len(unique_keys), dtype=int)
np.add.at(sums, inverse, amounts)

# Build result
result = []
for i, key in enumerate(unique_keys):
    sender, sender_bank, beneficiary, beneficiary_bank = key.split('|')
    result.append({
        "sender": sender,
        "sender_bank": sender_bank,
        "beneficiary": beneficiary,
        "beneficiary_bank": beneficiary_bank,
        "total_amount": sums[i]
    })

# Output
print(result)
print(result[1]['total_amount'])
# Goal: Identify which entries are expenses vs revenues and total each type
journal = [
    ("2025-06-01", "Cash", 5000, 0),
    ("2025-06-01", "Equity", 0, 5000),
    ("2025-06-02", "Utilities Expense", 900, 0),
    ("2025-06-02", "Cash", 0, 900),
    ("2025-06-04", "Cash", 3000, 0),
    ("2025-06-04", "Revenue", 0, 3000)
]

expenses = 0
revenues = 0

for entry in journal:
    account = entry[1].lower()
    if "expense" in account:
        expenses += entry[2]
    elif "revenue" in account:
        revenues += entry[3]

print("Total Expenses:", expenses)
print("Total Revenues:", revenues)
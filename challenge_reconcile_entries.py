# Goal: Flag any journal entries where debit ≠ credit
journal = [
    ("2025-06-01", "Cash", 5000, 0),
    ("2025-06-01", "Equity", 0, 5000),
    ("2025-06-02", "Office Supplies", 1000, 0),
    ("2025-06-02", "Cash", 0, 900) # ERROR: imbalance
]

print("Checking for entry imbalances...\n")
for i in range(0, len(journal), 2):
    debit = journal[i][2]
    credit = journal[i+1][3]
    if debit != credit:
        print("⚠️ Imbalance Detected:")
        print("  ", journal[i])
        print("  ", journal[i+1])
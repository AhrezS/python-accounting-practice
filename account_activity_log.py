# Goal: Create a dictionary that tracks how many times each account was used (not totals - just appearances)
journal = [
    ("2025-06-01", "Cash", 10000, 0),
    ("2025-06-01", "Equity", 0, 10000),
    ("2025-06-02", "Cash", 0, 1200),
    ("2025-06-03", "Revenue", 0, 2500),
    ("2025-06-04", "Cash", 3000, 0),
    ("2025-06-05", "Rent Expense", 1300, 0),
    ("2025-06-06", "Cash", 0, 1000)
]

account_usage = {}

for entry in journal:
    account = entry[1]
    account_usage[account] = account_usage.get(account, 0) + 1

print("Account Usage Count:")
for account, count in account_usage.items():
    print(f"{account}: {count} times")
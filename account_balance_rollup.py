# Goal: Show net balance of every account (debit - credit)
journal = [
    ("2025-06-01", "Cash", 10000, 0),
    ("2025-06-01", "Equity", 0, 10000),
    ("2025-06-02", "Office Supplies", 1200, 0),
    ("2025-06-02", "Cash", 0, 1200),
    ("2025-06-03", "Cash", 3000, 0),
    ("2025-06-03", "Revenue", 0, 3000)
]

account_balances = {}

for entry in journal:
    account = entry[1]
    debit = entry[2]
    credit = entry[3]

    if account not in account_balances:
        account_balances[account] = 0

    account_balances[account] += debit - credit

print("Net Balances by Account:")
for account, balance in account_balances.items():
    print(f"{account}: {balance}")
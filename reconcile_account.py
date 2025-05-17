journal = [
    ("2025-07-01", "Cash", 1000, 0),
    ("2025-07-01", "Office Supplies", 0, 1000),

    ("2025-07-02", "Cash", 2000, 0),
    ("2025-07-02", "Accounts Receivable", 0, 2000),

    ("2025-07-03", "Cash", 0, 500),
    ("2025-07-03", "Rent Expense", 500, 0)
]

def get_account_balances(journal):
    balances = {}
    for entry in journal:
        account = entry[1]
        debit = entry[2]
        credit = entry[3]

        if account not in balances:
            balances[account] = 0

        balances[account] += debit - credit
    return balances

# Official ledger balances
official = {
    "Cash": 2500,
    "Office Supplies": -1000,
    "Accounts Receivable": -2000,
    "Rent Expense": 500
}

journal_balances = get_account_balances(journal)

print("🔍 Reconciliation Report")
print("========================")

for account in official:
    system = journal_balances.get(account, 0)
    reported = official[account]

    if system == reported:
        print(f"{account}:✅ Balanced at {reported}")
    else:
        print(f"{account}:❌ Mismatch! System = {system}, Official = {reported}")
# Goal: Validate journal entries for correctness, summarize all account balances, reconcile each account with expected (ledger) balances, and provide a clean report of matched and unmatched accounts.
journal = [
    ("2025-08-01", "Cash", 1000, 0),
    ("2025-08-01", "Revenue", 0, 1000),

    ("2025-08-02", "Cash", 0, 500),
    ("2025-08-02", "Office Supplies", 500, 0),

    ("2025-08-03", "", 200, 200),       # Missing account
    ("2025-08-04", "Cash", -100, 0),    # Negative debit

    ("2025-08-05", "Accounts Receivable", 1500, 0),
    ("2025-08-05", "Revenue", 0, 1500),

    ("2025-08-06", "Cash", 0, 300),
    ("2025-08-06", "Bank Charges", 300, 0)
]

# Expected balances for reconciliation
expected_balances = {
    "Cash": 200,
    "Revenue": -2500,
    "Office Supplies": 500,
    "Accounts Receivable": 1500,
    "Bank Charges": 300
}

# Validate journal entries
for i in range(0, len(journal), 2):
    entry1 = journal[i]
    entry2 = journal[i+1]

    # Check for missing accounts
    if not entry1[1]:
        print(f"⚠️ Missing account from journal entry: {entry1}")
    if not entry2[1]:
        print(f"⚠️ Missing account from journal entry: {entry2}")

    # Check for negative debits/credits
    if entry1[2] < 0 or entry1[3] < 0:
        print(f"⚠️ Negative debit/credit in journal entry: {entry1}")
    if entry2[2] < 0 or entry2[3] < 0:
        print(f"⚠️ Negative debit/credit in journal entry: {entry2}")
    
    # Check for mismatched debits and credits
    if entry1[2] != entry2[3] or entry1[3] != entry2[2]:
        print(f"❌ Mismatched debits and credits in journal entries: {entry1} and {entry2}")

# Summarize account balances
# Initialize account balances
account_balances = {}

# Process journal entries
for entry in journal:
    date, account, debit, credit = entry
    
    # Skip any invalid entries
    if not account:
        continue

    if account not in account_balances:
        account_balances[account] = {"debit": 0, "credit": 0}

    account_balances[account]["debit"] += debit
    account_balances[account]["credit"] += credit

print("\nAccount Balances Summary:")
for account, balances in account_balances.items():
    print(f"{account:<25} | Debit: {balances['debit']:>6} | Credit: {balances['credit']:>6} | Balance: {balances['debit'] - balances['credit']:>6}")

# Reconcile accounts with expected balances
print("\n🔍 Reconciliation Report:\n")

for account, expected in expected_balances.items():
    actual_debit = account_balances.get(account, {}).get("debit", 0)
    actual_credit = account_balances.get(account, {}).get("credit", 0)
    actual_balance = actual_debit - actual_credit

    if actual_balance == expected:
        print(f"✅ {account:<25} matches expected balance: {expected}")
    else:
        print(f"❌ {account:<25} mismatch: Actual = {actual_balance}, Expected = {expected}")

# Create a list to store report lines
report_lines = []
report_lines.append("🔍 Reconciliation Report\n")

for account, expected in expected_balances.items():
    actual_debit = account_balances.get(account, {}).get("debit", 0)
    actual_credit = account_balances.get(account, {}).get("credit", 0)
    actual_balance = actual_debit - actual_credit

    if actual_balance == expected:
        line = f"✅ {account:<25} matches expected balance: {expected}"
    else:
        line = f"❌ {account:<25} mismatch: Actual = {actual_balance}, Expected = {expected}"
    
    print(line)  # still print to terminal
    report_lines.append(line)

# Export to a text file
with open("reconciliation_report.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")

from datetime import datetime

# At the top of your script
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"reconciliation_report_{timestamp}.txt"

# Then use this in your export
with open(filename, "w") as file:
    for line in report_lines:
        file.write(line + "\n")
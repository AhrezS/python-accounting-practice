# Challenge Journal Data (Date, Account, Debit, Credit)

journal = [
    ("2025-06-01", "Cash", 10000, 0),
    ("2025-06-01", "Loan Payable", 0, 10000),

    ("2025-06-02", "Office Supplies", 1200, 0),
    ("2025-06-02", "Cash", 0, 1200),

    ("2025-06-03", "Accounts Receivable", 2500, 0),
    ("2025-06-03", "Revenue", 0, 2500),

    ("2025-06-04", "Cash", 3000, 0),
    ("2025-06-04", "Accounts Receivable", 0, 3000),

    ("2025-06-05", "Rent Expense", 1300, 0),
    ("2025-06-05", "Cash", 0, 1300)
]

# Step 1: Tally account totals
account_totals = {}

for entry in journal:
    account = entry[1]
    debit = entry[2]
    credit = entry[3]

    if account not in account_totals:
        account_totals[account] = {'debit': 0,'credit': 0}

    account_totals[account]['debit'] += debit
    account_totals[account]['credit'] += credit

# Step 2: Print header
print("\nTrial Balance (June 2025)")
print("---------------------------")
print("Account              Debit       Credit")
print("---------------------------------------")

for account, totals in account_totals.items():
    print(f"{account:20} {totals['debit']:>8}     {totals['credit']:>8}")

# Step 3: Total Check (Debits=Credits?)
total_debits = 0
total_credits = 0

for totals in account_totals.values():
    total_debits += totals['debit']
    total_credits += totals['credit']

print("\nTotal Debits: ", total_debits)
print("Total Credits: ", total_credits)

from openpyxl import Workbook

# Create workbook and worksheet
wb = Workbook ()
ws = wb.active
ws.title = "Trial Balance"

# Headers
ws.append(["Account", "Debit", "Credit"])

# Add each account's totals
for account, totals in account_totals.items():
    ws.append([account, totals['debit'], totals['credit']])

# Add totals at bottom
ws.append(["Total", total_debits, total_credits])

# Save the file
wb.save("Trial_Balance_June_2025.xlsx")
print("\nExcel file saved successfully!")
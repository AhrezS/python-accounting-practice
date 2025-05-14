# Journal Entry System using Lists and Tuples

# Each entry is a tuple: (date, account, debit, credit)
entry1 = ("2025-05-01", "Cash", 25000, 0)
entry2 = ("2025-05-01", "Equity", 0, 25000)

entry3 = ("2025-05-02", "Equipment", 8000, 0)
entry4 = ("2025-05-02", "Cash", 0, 8000)

entry5 = ("2025-05-03", "Cash", 3000, 0)
entry6 = ("2025-05-03", "Revenue", 0, 3000)

# Store all entries in a list
journal = [entry1, entry2, entry3, entry4, entry5, entry6]

# Print them out in a clean way
print("Date       | Account    | Debit  | Credit")
print("---------------------------------------------")
for entry in journal:
    date, account, debit, credit = entry
    print(f"{date} | {account:10} | {debit:8} | {credit:7}")

# Bonus Exercise: Calculate total debits and credits
total_debits = 0
total_credits = 0
for entry in journal:
    total_debits += entry[2]
    total_credits += entry[3]

print("\nTotal Debits:", total_debits)
print("Total Credits:", total_credits)

# Practice 1: Print only Cash entries using for loop
for entry in journal:
    if entry[1] == "Cash":
        print(entry)

# Practice 2: Print just the account names and ammounts if debit > 0
for entry in journal:
    if entry[2] >0:
        print("Debit to", entry[1], "for", entry[2])

# Practice 3: Build a list of unique accounts used
unique_accounts = []

for entry in journal:
    if account not in unique_accounts:
        unique_accounts.append(account)

print("Accounts used:", unique_accounts)

# Exercise 1: Show all Debits only
for entry in journal:
    if entry[2] > 0:
        print(f"Debit - {entry[1]}: {entry[2]}")

# Exercise 2: Separate Debits and Credits
debit_accounts = []
credit_accounts = []

for entry in journal:
    if entry[2] > 0 and entry[1] not in debit_accounts:
        debit_accounts.append(entry[1])
    if entry[3] > 0 and entry[1] not in credit_accounts:
        credit_accounts.append(entry[1])

print("Debits:", debit_accounts)
print("Credits:", credit_accounts)

# Exercise 3: Calculate Account Totals
account_totals = {}

for entry in journal:
    account = entry[1]
    debit = entry[2]
    credit = entry[3]

    if account not in account_totals:
        account_totals[account] = {'debit':0, 'credit':0}

    account_totals[account]['debit'] += debit
    account_totals[account]['credit'] += credit

# Print totals neatly
for account, totals in account_totals.items():
    print(f"{account} -> Debit: {totals['debit']}, Credit: {totals['credit']}")

# Exercise 4: Filter Only Revenue Entries
for entry in journal:
    if entry[1] == "Revenue":
        print(entry)

# Exercise 5: Count Nmber of Times an Account Appears
account_count = {}

for entry in journal:
    account = entry[1]
    if account not in account_count:
        account_count[account] = 0
    account_count[account] += 1

print(account_count)
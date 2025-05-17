# Exercise: Is this entry balanced?
def is_entry_balanced(entry):
    debit = entry[2]
    credit = entry[3]
    if debit == credit:
        return True
    else:
        return False

# Test entries
entry1 = ("2025-07-01", "Cash", 5000, 5000)
entry2 = ("2025-07-02", "Office Supplies", 1000, 500)

print(is_entry_balanced(entry1)) # ✅ True
print(is_entry_balanced(entry2)) # ❌ False

# Exercise: Identifying account types
def check_account_type(account):
    account = account.lower()
    if "expense" in account:
        return "Expense"
    elif "revenue" in account:
        return "Revenue"
    elif "payable" in account or "loan" in account:
        return "Liability"
    else:
        return "Other"
    
print(check_account_type("Utilities Expense"))      # Expense
print(check_account_type("Unearned Revenue"))       # Revenue
print(check_account_type("Loan Payable"))           # Liability
print(check_account_type("Cash"))                   # Other

# Exercise: Writing a function that accepts a journal entry tuple, checks for missing values, checks if debit equals credit, and returns a verdict and message.
def validate_entry(entry):
    date, account, debit, credit = entry

    if not date or not account:
        return "❌ Missing date or account"
    
    if debit < 0 or credit < 0:
        return "❌ Negative debit or credit not allowed"
    
    if debit == credit:
        return "✅ Entry is balanced"
    else:
        return "⚠️ Debit and credit do not match"
    
# Sample tests
entries = [
    ("2025-07-01", "Cash", 1000, 1000),
    ("2025-07-02", "", 500, 500),
    ("2025-07-03", "Office Supplies", -100, 0),
    ("2025-07-04", "Revenue", 0, 900)
]

for e in entries:
    print(f"{e}: {validate_entry(e)}")
    
# Mini Challenge: Entry Scorecard
valid = 0
invalid = 0
warning = 0

for e in entries:
    result = validate_entry(e)
    
    if "✅" in result:
        valid += 1
    elif "❌" in result:
        invalid += 1
    elif "⚠️" in result:
        warning += 1

print("\nEntry Scorecard:")
print("Valid Entries:", valid)
print("Invalid Entries:", invalid)
print("Warnings:", warning)
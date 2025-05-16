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
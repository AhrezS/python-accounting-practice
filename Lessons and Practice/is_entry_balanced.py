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
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
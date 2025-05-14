# Goal: Summarize all transactions involving Accounts Receivable
journal = [
    ("2025-06-01", "Accounts Receivable", 5000, 0),
    ("2025-06-04", "Accounts Receivable", 0, 2000),
    ("2025-06-05", "Accounts Receivable", 0, 1500)
]

total_invoiced = 0
total_collected = 0

for entry in journal:
    if entry[1] == "Accounts Receivable":
        total_invoiced += entry[2]
        total_collected += entry[3]

outstanding = total_invoiced - total_collected
print("Invoiced:", total_invoiced)
print("Collected:", total_collected)
print("Outstanding A/R:", outstanding)
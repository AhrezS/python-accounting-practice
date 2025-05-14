# Goal: track only cash transactions and calculate net cash movement
journal = [
    ("2025-06-01", "Cash", 10000, 0),
    ("2025-06-02", "Cash", 0, 1200),
    ("2025-06-03", "Cash", 3000, 0),
    ("2025-06-04", "Cash", 0, 1300)
]

cash_in = 0
cash_out = 0

for entry in journal:
    if entry[1] == "Cash":
        cash_in += entry[2]
        cash_out += entry[3]

print("Cash Received:", cash_in)
print("Cash Spent:", cash_out)
print("Net Cash Change:", cash_in - cash_out)
# Goal: Create a dictionary that groups journal entries by date for date_based reporting.
journal = [
    ("2025-06-01", "Cash", 10000, 0),
    ("2025-06-01", "Equity", 0, 10000),
    ("2025-06-02", "Office Supplies", 1200, 0),
    ("2025-06-02", "Cash", 0, 1200),
    ("2025-06-03", "Cash", 3000, 0),
    ("2025-06-03", "Revenue", 0, 3000)
]

date_groups = {}

for entry in journal:
    date = entry[0]
    if date not in date_groups:
        date_groups[date] = []
    date_groups[date].append(entry)

# Display entries by date
for date, entries in date_groups.items():
    print(f"\nDate: {date}")
    for e in entries:
        print(f" {e[1]} | Debit: {e[2]} | Credit: {e[3]}")
import sys

def flush():
    sys.stdout.flush()

n = int(input())

yes_rows = set()
yes_cols = set()

for i in range(1, n + 1):
    print("c", i, i)
    flush()
    response = input().strip()
    if response == "yes":
        yes_rows.add(i)
        yes_cols.add(i)

# We need one more query to distinguish row vs column
# Pick one confirmed row and test it with another column
if yes_rows:
    r = next(iter(yes_rows))
else:
    r = 1
if yes_cols:
    c = next(iter(yes_cols))
else:
    c = 1

# Final declaration
print("!", r, c)
flush()

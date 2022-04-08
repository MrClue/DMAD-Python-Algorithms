import ttg

# https://pypi.org/project/truth-table-generator/

# Bits:
# 0 = false
# 1 = true

table = (ttg.Truths(['p', 'q'], ['(p = q) and (p xor q)'], ints=False))


print(table.as_prettytable())


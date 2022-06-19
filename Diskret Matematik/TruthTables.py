# This Python file uses the following encoding: utf-8

import ttg

# https://pypi.org/project/truth-table-generator/

# Bits:
# 0 = false
# 1 = true

"""
Antal rækker i tabel = 2^n
- n: unikke variabler

Fx. "p ∧ q ∧ r"
- n = 3
- Rækker = 2^n = 8
"""
#n = 3
#print("Table Rows:", 2**n)

"""
Examples of tables below
"""

# p V q
#table = (ttg.Truths(['p', 'q'], ['p or q'], ints=False))

# p ∧ q
#table = (ttg.Truths(['p', 'q'], ['p and q'], ints=False))

# p -> q
#table = (ttg.Truths(['p', 'q'], ['p => q'], ints=False))

# p = q
#table = (ttg.Truths(['p', 'q'], ['p = q'], ints=False))

# p xor q
#table = (ttg.Truths(['p', 'q'], ['p xor q'], ints=False))

# tror nok at "=" er "<->"
# (p = q) V (p xor q)
#table = (ttg.Truths(['p', 'q'], ['(p = q) and (p xor q)'], ints=False))

# p ∧ q ∧ r
#table = (ttg.Truths(['p', 'q', 'r'], ['p and q and r'], ints=False))

# (p ∧ q) ∨ (r ∧ ¬q)
#table = (ttg.Truths(['p', 'q', 'r'], ['(p and q) or (r and (-q))'], ints=False))

# if (p -> q og -p -> -q) then (p <-> q)
#table = (ttg.Truths(['p', 'q', 'r'], ['(p => q) and ((-p) => (-q))', 'p = q'], ints=False))


"""
Check om x er ækvivalent med y:
- lav tabel for x og y
- hvis begge er true/false ved samme conditions = ækvivalente
"""
# hvilke udsagn er ækvivalente med (p -> -q)?
table = (ttg.Truths(['p', 'q'], ['p => (-q)', 'p or (-q)'], ints=False))


print(table.as_prettytable())


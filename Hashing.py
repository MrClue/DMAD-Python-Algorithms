"""
open addressing functions
""" 

# define array length
m = 11

# linear probing
def lp(k):
    # ( h'(k) + i ) mod m
    print("Linear Probing:")
    print("Index:", + (k % m))

# double hashing
def dh(k, i):
    # ( h1(k) + i*h2(k) ) mod m
    print("Double Hashing:")
    print("Index:", + ((k % m) + i*(1+(k % (m-1)))) % m)

# quadratic probing
def qp(k, c1, c2, i):
    # ( h'(k) + c1*i + c2*i^2 ) mod m
    print("Quadratic Probing:")
    print("Index:", + (k + c1*i + c2*i**2) % m)


"""
1. først definer "h'(x)"
2. "hashfunktion" placere "h'(x)" værdien på "k" plads
"""
x = 26 # tal som skal indsættes
hashfunktion = (7*x + 4) % m # h'(x) --> definer efter opgave beskrivelse

# linear probing
lp(hashfunktion) # if collision; place on next empty slot

# quadratic probing
#qp(hashfunktion, 3, 1, 4) # if collision; i + 1

# double hashing
# --> ofte bruges bare "x" i denne funktion, fremfor "hashfunktion"
#dh(x, 0) # if collision; i + 1
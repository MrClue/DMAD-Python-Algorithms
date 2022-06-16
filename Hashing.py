"""
open addressing functions
""" 

# define array length
m = 11

# linear probing
def h(k):
    # ( h'(k) + i ) mod m
    print("Linear Probing:")
    print("Index:", + (k % m))

#h(10) # if collision; place on next empty slot

# double hashing
def h(k, i):
    # ( h1(k) + i*h2(k) ) mod m
    print("Double Hashing:")
    print("Index:", + ((k % m) + i*(1+(k % (m-1)))) % m)

#h(18, 0) # if collision; i + 1

# quadratic probing
def h(k, c1, c2, i):
    # ( h'(k) + c1*i + c2*i^2 ) mod m
    print("Quadratic Probing:")
    print("Index:", + (k + c1*i + c2*i**2) % m)

h(1, 3, 1, 4) # if collision; i + 1


"""
1. først udregn "h'(x)"
2. herefter placer værdien på "k" plads
"""
x = 17
# h'(x)... defineres efter opgave beskrivelse
print((3*x + 5) % m) # == 1


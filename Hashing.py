#
# open addressing functions
#

# define array length
m = 11

# linear probing
def h(k):
    # h(k) = k mod m
    print("Linear Probing:")
    print("Index:", + (k % m))

h(10) # if collision; place on next empty slot

# double hashing
def h(k, i):
    # ( h1(k) + i*h2(k) ) mod m
    print("Double Hashing:")
    print("Index:", + ((k % m) + i*(1+(k % (m-1)))) % m)

h(18, 0) # if collision; i + 1

# quadratic probing
def h(k, c1, c2, i):
    print("Quadratic Probing:")
    print("Index:", + (k + c1*i + c2*i**2) % m)

h(4, 1, 3, 1) # if collision; i + 1


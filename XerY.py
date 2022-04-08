import math

def log(a):
    log_version = 10
    return math.log(a, log_version)

# Compare run-times using asymptotic notation

def c1(x, y):
    # x er O(y)
    print("Case 1: x er O(y)")
    print(str(x)+" er <=("+str(y)+"): " + str(x <= y) + "\n")

def c2(x, y):
    # x er Ω(y) --- \u03A9
    print("Case 2: x er Omega(y)")
    print(str(x)+" er >=("+str(y)+"): " + str(x >= y) + "\n")

def c3(x, y):
    # x er ϴ(y) --- \u03F4
    print("Case 3: x er Theta(y)")
    print(str(x)+" er =("+str(y)+"): " + str(x == y) + "\n")

def c4(x, y):
    # x er o(y)
    print("Case 4: x er o(y)")
    print(str(x)+" er <("+str(y)+"): " + str(x < y) + "\n")

def c5(x, y):
    # x er ω(y) --- \u03C9
    print("Case 5: x er w(y)")
    print(str(x)+" er >("+str(y)+"): " + str(x > y) + "\n")

# defining n to some random large number (to compute results)
n = 123

# output
#c1(1, math.sqrt(n)) # f1 = 1, g1 = sqrt(n)
#c1(n**2, n**3) # f2 = n^2, g2 = n^3

print("(a)")
c1(1 + n**2, math.sqrt(n) + n**3)

print("(b)")
c2(math.sqrt(n) + n**3, 1 + n**2)

print("(c)")
c1(1/n**2, math.sqrt(n)/n**3)
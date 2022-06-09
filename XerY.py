# This Python file uses the following encoding: utf-8

import math

def log(a):
    log_version = 10
    return math.log(a, log_version)

# defining n to some random large number (to compute results)
n = 123456789

# Compare run-times using asymptotic notation

def c1(x, y):
    # x er O(y)
    print("Case 1: x er O(y)")
    print(str(x)+" er <=("+str(y)+"): " + str(x <= y) + "\n")
#    if (x >= n and y >= n): # x og y har "n" condition
#        print(str(x)+" er <=("+str(y)+"): " + str(x <= y) + "\n")

#    if (x >= n and y < n): # x = "n" condition, y = konstant
#        print("False" + "\n")

#    if (x < n and y >= n): # x = konstant, y = "n" condition
#        print("TRUE" + "\n")

#    if (x < n and y < n): # x og y = konstanter
#        print("TRUE" + "\n")

#    else: # original
#        print(str(x)+" er <=("+str(y)+"): " + str(x <= y) + "\n")

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

# Noter:
# - "kvadratrod(x)" er "math.sqrt(x)"
# - "n^2" er "n**2"
# - Konstanter "(1,2,3...)" har altid samme voksehastighed! De er altid lavest voksehastighed i forhold til andre!

# OUTPUT:
#c1(x, y) # x er O(y) --- Konstanter (1,2,3...) er altid = TRUE, (konstant voksehastighed)!
#c2(x, y) # x er Ω(y)
#c3(x, y) # x er ϴ(y)
#c4(x, y) # x er o(y)
#c5(x, y) # x er ω(y)

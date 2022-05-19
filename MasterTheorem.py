# This Python file uses the following encoding: utf-8

# Master Theorem Calculator
# By Yusaf Tareen
# Logic inspiration: https://github.com/hamza1886/master-theorem

import math

# Divide and Conquer (DaC)
# T(n) = aT(n/b) + f(n), where
#   a >= 1
#   b > 1
#   f(n) = O(n^d log^k n), where 
#       d >= 0 and k >= 0

def DaC(a, b, d, k):
    print("Input recurrence: T(n) = "+str(a)+"T(n/"+str(b)+") + O(n^"+str(d)+" * log^"+str(k)+"(n))"+"\n")

    print("Using: Divide and Conquer!")
    # check main constants
    if (a >= 1 and b > 1 and d >= 0):
        # case 1: log_b(a) > d
        if (math.log(a, b) > d):
            result = math.log(a, b)
            print("Running case 1: log_b(a) > d")
            # prettify result
            if (result != 1): print("T(n) = O(n^"+str(math.log(a, b))+")")
            else: print("T(n) = O(n)")

        # case 2: log_b(a) = d
        elif (math.log(a, b) == d):
            # prettify d
            if (d == 1): d = ""
            else: d = "^"+str(d)

            print("Running case 2: log_b(a) = d")
            if (k > -1):
                if (k+1 != 1):
                    print("T(n) = O(n"+str(d)+" log^"+str(k+1)+" n)")
                else: print("T(n) = O(n"+str(d)+" log n)") # pretty k
            elif (k == -1):
                print("T(n) = O(n"+str(d)+" log log n)")
            elif (k < -1):
                print("T(n) = O(n"+str(d)+")")
        
        # case 3: log_b(a) < d
        elif (math.log(a, b) < d):
            # prettify d
            if (d == 1): d = ""
            else: d = "^"+str(d)

            print("Running case 3: log_b(a) < d")
            if (k > 0):
                if (k != 1): print("T(n) = O(n"+str(d)+" log^"+str(k)+" n)")
                else: print("T(n) = O(n"+str(d)+" log n)") # pretty k
            elif (k <= 0):
                print("T(n) = O(n"+str(d)+")")
    else:
        print("Invalid input!")

# Subtract/Decrease and Conquer (V2)
# T(n) = aT(n-b) + f(n)
#   a > 0, 
#   b > 0, 
#   f(n) = O(n^d log^k n), where
#       d >= 0 and k >= 0
 
def SaC(a, b, d, k):
    print("Input recurrence: "+ "T(n) = "+str(a)+"T(n-"+str(b)+") + O(n^"+str(d)+" * log^"+str(k)+"(n))"+"\n")

    # prettify result
    if (k == 0): k = ""
    elif (k == 1): k = " log(n)"
    else: k = " log^"+str(k)+"(n)"

    if (d == 0 and a != 1): d = ""
    elif (d == 1 and a != 1 and a < 1): d = "n" # case 1 only
    elif (d == 1 and a != 1): d = " n"
    elif (d > 1 and a != 1 and a < 1): d = "n^"+str(d) # case 1 only
    elif (d > 1 and a != 1): d = " n^"+str(d)

    print("Using: Decrease and Conquer!")
    if (a > 0 and b > 0):
        # case 1: a < 1
        if (a < 1):
            print("Running case 1: a < 1")
            #print("T(n) = O(n^"+str(d)+" log^"+str(k)+" n)")
            print("T(n) = O("+d+k+")")

        # case 2: a = 1
        elif (a == 1):
            print("Running case 2: a = 1")
            #print("T(n) = O(n^"+str(d+1)+" log^"+str(k)+" n)")
            print("T(n) = O(n^"+str(d+1)+k+")") #pretty

        # case 3: a > 1
        elif (a > 1):
            print("Running case 3: a > 1")
            #print("T(n) = O("+str(a)+"^n/"+str(b)+" n^"+str(d)+" log^"+str(k)+" n)")
            print("T(n) = O("+str(a)+"^n/"+str(b)+d+k+")") #pretty
    else: 
        print("Invalid input!")

# Lets compute solution for T(n) using Divide and Conquer (DaC)
DaC(16, 2, 4, 1)

# Lets compute solution for T(n) using Decrease and Conquer (SaC)
#SaC(1, 1, 1, 0)

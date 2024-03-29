# This Python file uses the following encoding: utf-8

# Strassen's Method for multiplying n x n matrixes
# Time Complexity: T(n) = 7T(n/2) + O(n^2)
# which is: ϴ(n^log7) or O(n^2.81)

import math
import numpy as np

def Strassen(A, B):
    # define indexes
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    e = B[0]
    f = B[1]
    g = B[2]
    h = B[3]

    # recursive calls
    p1 = a*(f-h)
    p2 = (a+b)*h
    p3 = (c+d)*e
    p4 = d*(g-e)
    p5 = (a+d)*(e+h)
    p6 = (b-d)*(g+h)
    p7 = (a-c)*(e+f)

    matrix_c = np.array([[p5+p4-p2+p6, p1+p2], [p3+p4, p1+p5-p3-p7]])
    
    print("Matrix C:")
    for line in matrix_c:
        print('  '.join(map(str, line)))
    

# define matrix a & b
matrix_a = [1, 3, 7, 5]
matrix_b = [6, 8, 4, 2]

# Output
Strassen(matrix_a, matrix_b)

# ------------------
# 2nd implementation from Geeks4Geeks

def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
def strassen(x, y):
    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """
 
    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y
 
    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h) 
    p2 = strassen(a + b, h)       
    p3 = strassen(c + d, e)       
    p4 = strassen(d, g - e)       
    p5 = strassen(a + d, e + h)       
    p6 = strassen(b - d, g + h) 
    p7 = strassen(a - c, e + f) 
 
    # Computing the values of the 4 quadrants of the final matrix c
    c11 = p5 + p4 - p2 + p6 
    c12 = p1 + p2          
    c21 = p3 + p4           
    c22 = p1 + p5 - p3 - p7 
 
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
 
    return c

#x1 = np.array([[1, 3], [7, 5]])
#x2 = np.array([[6, 8], [4, 2]])
#print(strassen(x1, x2))
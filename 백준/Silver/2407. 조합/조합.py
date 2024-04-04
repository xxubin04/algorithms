from itertools import combinations
from fractions import Fraction

input = open(0).readline 
n, m = map(int, input().split())

def factorial(a, result):
    if a >= 2:
        result *= a
        return factorial(a-1, result)
    else:
        return result
        
print(Fraction(factorial(n, 1), (factorial(n-m, 1)*factorial(m, 1))))
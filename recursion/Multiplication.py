'''Given two integers M & N, calculate and return their multiplication using recursion. 
You can only use subtraction and addition for your calculation. No other operators are allowed.'''

def multiplication(m,n):
    if n==0:
        return 0
    if n==1:
        return m
    return m+multiplication(m,n-1)


from sys import setrecursionlimit
setrecursionlimit(10**6) 
m=int(input())
n=int(input())
print(multiplication(m,n))

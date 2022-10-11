#finding factorial of n 
'''to avoid max recursion depth exceeded error in our program
#when we input large numbers, we can use the following'''
import sys
sys.setrecursionlimit(10000)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=int(input())
print(fact(n))

'''base case : n=0
hypothesis : fact(n-1) {if this works then induction step will def work}
induction step : fact(n)'''

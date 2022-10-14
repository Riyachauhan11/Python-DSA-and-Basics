#Given an array of length N, you need to find and return the sum of all elements of the array.
#Do this recursively.

def sumArray(arr,si):
    # Please add your code here
    l=len(arr)
    if si==l-1:
        return 0   
    hypot=sumArray(arr,si+1)+arr[si+1]
    return hypot

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr,-1))

#You have been given an integer array/list(ARR) of size N that contains only integers,
#0 and 1. Write a function to sort this array/list. Think of a solution which scans the
#array/list only once and don't require use of an extra array/list.


def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    si=0
    ei=n-1
    while si<=ei:
        if arr[si]!=1:
            si+=1
        if arr[ei]!=0:
            ei-=1
        if arr[si]==1 and arr[ei]==0:
            arr[si],arr[ei]=arr[ei],arr[si]
            si+=1
            ei-=1
            


t=int(input())
for i in range(t):
    n=int(input())
    if n!=0:
        arr=[int(x) for x in input().split()]
        sorted=sortZeroesAndOne(arr,n)
        for ele in arr:
           print(ele,end=' ')
        print()

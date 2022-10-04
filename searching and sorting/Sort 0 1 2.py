#You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. 
#Write a solution to sort this array/list in a 'single scan'.
#'Single Scan' refers to iterating over the array/list just once or to put it in other words, 
#you will be visiting each element in the array/list just once.

def sort012(arr, n) :
    #Your code goes here
    i=0
    nz=0
    nt=n-1
    while i<=nt:
        if arr[i]==0:
            arr[i],arr[nz]=arr[nz],arr[i]
            i+=1
            nz+=1
        elif arr[i]==1:
            i+=1
        elif arr[i]==2:
            arr[i],arr[nt]=arr[nt],arr[i]
            nt-=1
        
t=int(input())
for i in range(t):
    n=int(input())
    if n!=0:
        arr=[int(x) for x in input().split()]
        sorted=sort012(arr,n)
        for ele in arr:
           print(ele,end=' ')
        print()

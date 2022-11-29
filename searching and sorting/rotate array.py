#You have been given a random integer array/list(ARR) of size N. 
#Write a function that rotates the given array/list by D elements(towards the left).

def rotate(arr, n, d):
    #Your code goes here
    for i in range(d):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
            print(arr)
        arr[n-1]=temp

t=int(input())
for i in range(t):
    n=int(input())
    if n!=0:
        arr=[int(x) for x in input().split()]
    else:
        arr=[]
    d=int(input())
    rotate(arr,n,d)
    for ele in arr:
       print(ele,end=' ')
    print()
    
------------------------------------------------------------------------------------

#easier soln

def rotate (arr, n, d):
    arr.reverse()
    part_1=arr[0:(n-d)]
    part_2=arr[(n-d):]
    part_1.reverse()
    part_2.reverse()
    return part_1+part_2


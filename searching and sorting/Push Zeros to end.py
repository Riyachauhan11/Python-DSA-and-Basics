#You have been given a random integer array/list(ARR) of size N. 
#You have been required to push all the zeros that are present in the array/list to the end of it. 
#Also, make sure to maintain the relative order of the non-zero elements.
#t indicates test cases,n represents length of array.

def pushZerosAtEnd(arr, n) :
    #Your code goes here
    k=0
    i=0
    for j in range(n):
        if i>k and arr[i]!=0:
            arr[i],arr[k]=arr[k],arr[i]
            k+=1
            i+=1
        elif arr[i]==0:
            i+=1
        else:
            i+=1
            k+=1       
    
t=int(input())
for i in range(t):
    n=int(input())
    if n!=0:
        arr=[int(x) for x in input().split()]
        sorted=pushZerosAtEnd(arr,n)
        for ele in arr:
           print(ele,end=' ')
        print()

#You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
#Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
#You need to find and return that number which is unique in the array/list.
#t refers to test cases and in input array 1 Unique element is always present.

def findUnique(arr, n) :
    #Your code goes here
    for j in range(n):
        count=0
        for i in range(n):
            if arr[i]==arr[j]:
                count+=1
            if count>1:
                break
        if count==1:
            return j        
        
t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    unique=findUnique(arr,n)
    print(arr[unique])

#You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
#Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
#You need to find and return that number which is unique in the array/list.
#in input array 1 Unique element is always present.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.


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
    
    
    ---------------------------------------------
    
    # better solution as per space and time complexity
    
    def findUnique(arr, n):
    #Your code goes here
    i=0
    if n==1:
        print(arr[0])
    while i<n-1:
        if arr[i]==arr[i+1]:
            i+=2
            if i==n-1:
                if arr[i]!=arr[i-1]:
                    print(arr[i])
                    break
        else:
            print(arr[i])
            break

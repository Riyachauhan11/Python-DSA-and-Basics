#You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the array/list which sum to X.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.
#Third line contains an integer 'X'.

def pairSum(arr, n, x) :
    #Your code goes here
    count=0
    for i in range(n):
        for j in range(i+1,n):
            comp=arr[i]+arr[j]
            if comp==x:
                count+=1        
    return count
            
t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    if n!=0:
        x=int(input())
        pairs=pairSum(arr,n,x)
        print(pairs)
    else:
        print(0)

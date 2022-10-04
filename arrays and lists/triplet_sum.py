#You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.
#Third line contains an integer 'X'.

def findTriplet(arr, n, x) :
    #Your code goes here
    count=0
    loop_c=n-2
    for i in range(n):
        p=i+1
        k=i
        for b in range(loop_c):
            for j in range(k+2,n):
                comp=arr[i]+arr[p]+arr[j]
                #print(comp)
                if comp==x:
                    count+=1
            p+=1
            k+=1
        loop_c-=1
    return count

    #return your answer

t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    if n!=0:
        x=int(input())
        triplets=findTriplet(arr,n,x)
        print(triplets)
    else:
        print(0)

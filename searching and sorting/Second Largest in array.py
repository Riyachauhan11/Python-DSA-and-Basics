#You have been given a random integer array/list(ARR) of size N. 
#You are required to find and return the second largest element present in the array/list.
#If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)

def secondLargestElement(arr, n):
    #Your code goes here
    largest=-2147483648
    second_l=-2147483648
    for i in range(n):
        if arr[i]>largest:
            second_l=largest
            largest=arr[i]
        if arr[i]>second_l and arr[i]!=largest:
            second_l=arr[i]
    return second_l      

                        
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    if n<=1:
        print(-2147483648)
    else:
        arr=[int(x) for x in input().split()]
        for i in arr:
            if i==arr[0]:
                count+=1
        if count!=len(arr):
            second=secondLargestElement(arr, n)
            print(second)
        else :
            print(-2147483648)

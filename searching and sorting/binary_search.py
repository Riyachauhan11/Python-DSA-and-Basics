#You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X.
#Write a function to search this element in the given input array/list using 'Binary Search'.Return
#the index of the element in the input array/list. In case the element is not present in the array/list, then return -1.

#The first line contains an Integer 'N' which denotes the size of the array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.
#Third line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow..
#All the 't' lines henceforth, will take the value of X to be searched for in the array/list.

def binarySearch(arr, n, x) :
    #Your code goes here
    si=0
    ei=len(arr)-1
    while si<=ei:
        mid=(si+ei)//2
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            si=mid+1
        else:
            ei=mid-1
    else:
        return -1
                
    
n=int(input())
if n!=0:
    arr=[int(x) for x in input().split()]
else:
    arr=[]
t=int(input())
for i in range(t):
    x=int(input())
    index=binarySearch(arr, n, x)
    print(index)

    
    

#Finding first occurrence of the given number
def binarySearch(arr, n, x) :
    #Your code goes here
    si=0
    ei=len(arr)-1
    count=0
    while si<=ei:
        mid=(si+ei)//2
        if x==arr[mid]:
            a=mid-1
            while x==arr[a]:
                count+=1
                a-=1                
            return mid-count
        elif x>arr[mid]:
            si=mid+1
        else:
            ei=mid-1
    else:
        return -1
                
    
n=int(input())
if n!=0:
    arr=[int(x) for x in input().split()]
else:
    arr=[]
t=int(input())
for i in range(t):
    x=int(input())
    index=binarySearch(arr, n, x)
    print(index)
    
    
    

#Finding the last occurrence of the given number.
def binarySearch(arr, n, x) :
    #Your code goes here
    si=0
    ei=len(arr)-1
    count=0
    while si<=ei:
        mid=(si+ei)//2
        if x==arr[mid]:
            a=mid+1
            while x==arr[a]:
                count+=1
                a+=1      
                if a==len(arr):
                    break
            return mid+count
        elif x>arr[mid]:
            si=mid+1
        else:
            ei=mid-1
    else:
        return -1
                
    
n=int(input())
if n!=0:
    arr=[int(x) for x in input().split()]
else:
    arr=[]
t=int(input())
for i in range(t):
    x=int(input())
    index=binarySearch(arr, n, x)
    print(index)

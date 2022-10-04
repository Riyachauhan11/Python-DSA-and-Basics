#Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble Sort'.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.

def bubbleSort(arr, n) :
    #Your code goes here
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                            

t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    bubbleSort(arr, n)
    for ele in arr:
        print(ele,end=' ')
    print()

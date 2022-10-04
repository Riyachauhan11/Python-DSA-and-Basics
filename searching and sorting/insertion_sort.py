#Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Insertion Sort'.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list

def insertionSort(arr, n) :  
    #Your code goes here
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
        


t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    insertionSort(arr, n)
    for ele in arr:
        print(ele,end=' ')
    print()

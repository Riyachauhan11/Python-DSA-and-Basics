'''Given an integer array of size N. Sort this array (in decreasing order) using heap sort.
Note: Space complexity should be O(1).'''

def down_heapify(arr,i,n):

    parentIndex=i
    leftChildIndex=2*parentIndex + 1
    rightChildIndex=2*parentIndex +2

    while leftChildIndex < n:
        min_index=parentIndex
        
        if arr[min_index]>arr[leftChildIndex]:
            min_index=leftChildIndex
        if rightChildIndex<n and arr[min_index]>arr[rightChildIndex]:
            min_index=rightChildIndex
        
        if min_index==parentIndex:
            return
        
        arr[min_index],arr[parentIndex]=arr[parentIndex],arr[min_index]
        parentIndex=min_index
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2
    return 


def heapSort(arr):
    #Build the heap
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        down_heapify(arr,i,n)

    #Removing n elements from heap and put them at correct position
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heapify(arr,0,i)

    arr.reverse()
    return


n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')

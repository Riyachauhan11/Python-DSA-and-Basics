def quickSort(arr, start, end):
    # Please add your code here
    if start>=end:
        return
    pivot_index=partition(arr,start,end)
    quickSort(arr,start,pivot_index-1)
    quickSort(arr,pivot_index+1,end)
    
def partition(arr,start,end):
    pivot=arr[start]
    count=0
    for i in range(start,end+1):
        if arr[i]<pivot:
            count+=1
    arr[start],arr[start+count]=arr[start+count],arr[start]
    pivot_index=start+count
    i=start
    j=end
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return pivot_index               

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)


'''not a very different answer'''

def quickSort(arr, start, end):
    # Please add your code here
    if start>=end:
        return
    index=partition(arr,start,end)
    quickSort(arr,start,index-1)
    quickSort(arr,index+1,end)
    
def partition(arr,start,end):
    count=start
    pivot=arr[start]
    for i in range(start,end+1):
        if arr[i]<pivot:
            count+=1
    arr[start],arr[count]=arr[count],arr[start]
    i=start
    j=end
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return count                 

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)



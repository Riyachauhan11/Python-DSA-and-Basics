def mergeSort(arr, start, end):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return arr
    mid=(start+end)//2
    s1=arr[0:mid]
    s2=arr[mid:]
    mergeSort(s1,0,len(s1))
    mergeSort(s2,0,len(s2))
    merge(s1,s2,arr)
    
def merge(s1,s2,arr):
    i=0
    j=0
    index=0
    while i<len(s1) and j<len(s2):
        if s1[i]>s2[j]:
            arr[index]=s2[j]
            j+=1
            index+=1
        else:
            arr[index]=s1[i]
            i+=1
            index+=1
    if i==len(s1):
        while index<len(arr):
            arr[index]=s2[j]
            index+=1
            j+=1
    else:
        while index<len(arr):
            arr[index]=s1[i]
            i+=1
            index+=1
        
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)


'''without using starting index and ending index in merge sort func (not a very different answer)'''

def merge(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1


def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]
    
    merge_sort(a1)
    merge_sort(a2)
    merge(a1,a2,a)


'''You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. 
You need to print their intersection; 
An intersection for this problem can be defined when both the arrays/lists contain a particular value 
or to put it in other words, when there is a common value that exists in both the arrays/lists.
Input arrays/lists can contain duplicate elements.'''

# t in program refers to test cases

# Time complexity - O(n*log(n)+m*log(m)) [both are coming from sorting of 2 lists]

def intersection(arr1, arr2, n, m) :
	#Your code goes here
    arr1.sort()
    arr2.sort()
    i=0
    j=0
    while i<n  and j<m:
        if arr1[i]==arr2[j]:
            print(arr1[i],end=' ')
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    print()
    
  
'''another solution'''

# Time complexity - O(n*log(n)+m*log(n)) 
# [n being the length of smaller list, 
# so n*logn refers to the sorting and m*log(n) 
# calls out the m no of times we will be doing binary search]

def intersection(arr1, arr2, n, m) :
	#Your code goes here
    i,j=0,0
    if n<m:
        arr1.sort()
        while j<len(arr2):
            binary_search(arr1,arr2[j],0,len(arr1)-1)
            j+=1
    else:
        arr2.sort()
        while i<len(arr1):
            binary_search(arr2,arr1[i],0,len(arr2)-1)
            i+=1
    
def binary_search(arr, x, si, ei):
    if si > ei:
        return 
    mid = (si+ei)//2
    if arr[mid] == x:
        print(x,end=' ')
        arr.remove(x)
    elif arr[mid] > x:
        return binary_search(arr, x, si, mid-1)
    else:
        return binary_search(arr, x, mid+1, ei)


    
  


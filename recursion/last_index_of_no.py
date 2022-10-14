#Given an array of length N and an integer x, you need to find 
#and return the last index of integer x present in the array.
#Return -1 if it is not present in the array.
#Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
#You should start traversing your array from 0, not from (N - 1).
#Do this recursively. Indexing in the array starts from 0.

'''using list slicing'''
def last_Index(arr,x):
    l=len(arr)
    if l==0:
        return -1
    smaller_list=arr[1:]
    smaller_list_output=last_Index(smaller_list,x)
    if arr[0]==x:
        return smaller_list_output+1
    if smaller_list_output!=-1:
        return smaller_list_output+1
    else:
        return -1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(last_Index(arr, x))


'''using starting index (better solution - explained why in check_sorted_list.py)'''
def last_Index(arr,x,si):
    l=len(arr)
    if si==l:
        return -1
    output=last_Index(arr,x,si+1)
    if output!=-1:
        return output
    else:
        if arr[si]==x:
            return si
        else:
            return -1
        
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(last_Index(arr, x,0))
                      

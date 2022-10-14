'''using list slicing'''
def firstIndex(arr, x):
    # Please add your code here
    l=len(arr)
    if l==0:
        return -1       
    if arr[0]==x:
        return 0
    small_list=arr[1:]
    SmallerListOutput=firstIndex(small_list,x)
    if SmallerListOutput != -1:
        return SmallerListOutput+1
    else:
        return -1

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))


'''using starting index (better solution)'''
def firstIndex(arr, x,si):
    # Please add your code here
    l=len(arr)
    if si==l:
        return -1       
    if arr[si]==x:
        return si
    return firstIndex(arr, x,si+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x,0))

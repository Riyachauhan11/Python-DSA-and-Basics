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
                      
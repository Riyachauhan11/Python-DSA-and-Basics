#You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, 
#merge them into a third array/list such that the third array is also sorted.
#t refers to the test cases , n and m are the lengths of 2 arrays

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        elif arr2[j]<=arr1[i]:
            arr.append(arr2[j])
            j+=1
    if i>=n:
        for k in range(j,len(arr2)):
            arr.append(arr2[k])
    elif j>=m:
        for k in range(i,len(arr1)):
            arr.append(arr1[k])


t=int(input())
for i in range(t):
    arr=[]
    n=int(input())
    if n!=0:
        arr1=[int(x) for x in input().split()]
    else:
        arr1=[]
    m=int(input())
    if m!=0:
        arr2=[int(x) for x in input().split()]
    else:
        arr2=[]
    merge(arr1, n, arr2, m)
    for ele in arr:
        print(ele,end=' ')
    print()

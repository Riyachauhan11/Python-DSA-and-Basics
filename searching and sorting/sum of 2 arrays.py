#Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. 
#Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). 
#The idea here is to represent each array/list as an integer in itself of digits N and M.
#You need to find the sum of both the input arrays/list treating them as two integers and put 
#he result in another array/list i.e. output array/list will also contain only single digit at every index.

def sumOfTwoArrays(arr1, n, arr2, m):
    #Your code goes here
    result=[]
    if n>m:
        count=n
    else:
        count=m
    i=n-1
    j=m-1
    carry=0
    for k in range(count):
        num=arr1[i]+arr2[j]+carry
        carry=num//10
        dig=num%10
        result.append(dig)
        i-=1
        j-=1
        if i<0 :
            arr1[i]=0
        if j<0:
            arr2[j]=0   
    result.insert(count+1,carry)
    result.reverse()   
    return result
    
    
t=int(input())
for i in range(t):
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
    if n!=0 and m!=0:
        lis=sumOfTwoArrays(arr1, n, arr2, m)
        for ele in lis:
            print(ele,end=' ')
        print()
    elif n!=0 and m==0:
        for i in range(n+1):
            arr2.append(0)
        lis=sumOfTwoArrays(arr1, n, arr2, m)
        for ele in lis:
            print(ele,end=' ')
        print()   
    elif m!=0 and n==0:
        for i in range(m+1):
            arr1.append(0)
        lis=sumOfTwoArrays(arr1, n, arr2, m)
        for ele in lis:
            print(ele,end=' ')
        print()   
    else:
        print(0)

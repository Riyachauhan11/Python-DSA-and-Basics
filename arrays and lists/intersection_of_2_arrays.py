#You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively.
#You need to print their intersection; An intersection for this problem can be defined when
#both the arrays/lists contain a particular value or to put it in other words, when there is 
#a common value that exists in both the arrays/lists.

#Input arrays/lists can contain duplicate elements.
#The intersection elements printed would be in the order they appear in the first array/list(ARR1)

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#Second line contains 'N' single space separated integers representing the elements of the first the array/list.
#Third line contains an integer 'M' representing the size of the second array/list.
#Fourth line contains 'M' single space separated integers representing the elements of the second array/list.

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    li=[]
    for i in range(n):
        count=0
        for index in range(m):
            if arr2[index]==arr1[i]:
                count+=1    
        if count>=1:
            li.append(arr1[i])
            arr2.remove(arr1[i])
            m=len(arr2)
    return li

t=int(input())
for i in range(t):
    n=int(input())
    if n!=0:
        arr1=[int(x) for x in input().split()]
    m=int(input())
    if m!=0:
        arr2=[int(x) for x in input().split()]
    if n!=0 and m!=0:
        lis=intersections(arr1, n, arr2, m)
        for ele in lis:
            print(ele,end=' ')
        print()
                                            

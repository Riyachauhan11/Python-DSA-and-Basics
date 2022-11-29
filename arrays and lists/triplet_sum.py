#You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.

#The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#Second line contains 'N' single space separated integers representing the elements in the array/list.
#Third line contains an integer 'X'.

def findTriplet(arr, n, x) :
    #Your code goes here
    count=0
    loop_c=n-2
    for i in range(n):
        p=i+1
        k=i
        for b in range(loop_c):
            for j in range(k+2,n):
                comp=arr[i]+arr[p]+arr[j]
                #print(comp)
                if comp==x:
                    count+=1
            p+=1
            k+=1
        loop_c-=1
    return count

    #return your answer

t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    if n!=0:
        x=int(input())
        triplets=findTriplet(arr,n,x)
        print(triplets)
    else:
        print(0)
        

-----------------------------------------------------------------------------------

# better soln

'''
Time complexity - O(n^2)
Space complexity - O(1)
where n is the size of input arr/list
'''

from sys import *

def triplet_sum(arr, n, target):

    num_triplets = 0
    arr.sort()

    for i in range(n):
        pair_sum_for = target-arr[i]
        num_pairs = Pair_Sum(arr, i+1, n-1, pair_sum_for)
        # i+1 --> si and n-1 --> ei
        num_triplets += num_pairs

    return num_triplets


def Pair_Sum(arr, i, j, num):

    count = 0

    while i < j:
        if arr[i]+arr[j] < num:
            i += 1
        elif arr[i]+arr[j] > num:
            j -= 1
        else:
            initial_left_element = arr[i]
            initial_left_index = i

            initial_right_element = arr[j]
            initial_right_index = j

            while i < j and arr[i] == initial_left_element:
                i += 1
            while j >= i and arr[j] == initial_right_element:
                j -= 1

            if initial_left_element == initial_right_element:
                equal_numbers = (i-initial_left_index) + \
                    (initial_right_index-j)-1
                count += ((equal_numbers)*(equal_numbers+1))//2

            else:
                count += (i-initial_left_index)*(initial_right_index-j)

    return count




#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(triplet_sum(arr, n, num))

    t -= 1


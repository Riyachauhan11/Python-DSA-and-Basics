'''For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] 
is equal to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, 
the item at the index 'i' is not included in either part.

If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned. 
Negative one(-1) if no such index is present.'''


'''
Time complexity - O(n)
Space complexity - O(1)

where n is the size of input arr/list
'''


from sys import stdin

def arrayEquilibriumIndex(arr, n,lsum,rsum,eq_i) :
    #Your code goes here
    if lsum==rsum:
        return eq_i
    elif eq_i==n-2:
        return -1
    lsum+=arr[eq_i]
    rsum-=arr[eq_i+1]
    return arrayEquilibriumIndex(arr, n,lsum,rsum,eq_i+1)


#Taking input using fast I/O method
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
    if n!=0:
        ts = 0
        i = 0
        while i < len(arr):
            ts += arr[i]
            i += 1
        left_sum = 0
        index = 0
        while index < len(arr):
            right_sum = ts-arr[index]-left_sum
            if right_sum == left_sum:
                print(index)
                break
            left_sum += arr[index]
            index += 1
        if index == len(arr):
            print(-1)
    else:
        print(-1)

    t-= 1

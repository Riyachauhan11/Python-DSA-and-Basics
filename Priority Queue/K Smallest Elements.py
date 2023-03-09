'''You are given with an integer k and an array of integers that contain numbers in random order. 
Write a program to find k smallest numbers from given array. You need to save them in an array and return it.
Time complexity should be O(n * logk) and space complexity should not be more than O(k).
Note: Order of elements in the output is not important.

Sample Input 1 :

13
2 12 9 16 10 5 3 20 25 11 1 8 6 
4

Sample Output 1 :

1 2 3 5 
'''

import heapq
def kSmallest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    smaller_list=lst[0:k]
    heapq._heapify_max(smaller_list)

    for i in range(k,len(lst)):
        if smaller_list[0]>lst[i]:
            heapq._heapreplace_max(smaller_list,lst[i])

    return smaller_list



# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')

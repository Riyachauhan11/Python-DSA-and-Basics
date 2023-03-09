'''Given an array A of random integers and an integer k, find and return the kth largest element in the array.
Note: Try to do this question in less than O(N * logN) time.

Sample Input 1 :

6
9 4 8 7 11 3
2

Sample Output 1 :

9
'''

mport heapq
def kthLargest(lst, k):
    ######################
    #PLEASE ADD CODE HERE#
    ######################

    smaller_list=lst[0:k]
    heapq.heapify(smaller_list)

    for i in range(k,len(lst)):
        if smaller_list[0]<lst[i]:
            heapq.heapreplace(smaller_list,lst[i])


    return smaller_list[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)

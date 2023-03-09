'''Given an array of integers, check whether it represents max-heap or not. Return true if the given array represents max-heap, else return false.
Sample Input 1:

8
42 20 18 6 14 11 9 4

Sample Output 1:

true

'''

def checkMaxHeap(arr):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################

    l=len(arr)
    non_leaf_count=l//2
    flag=True

    for i in range(0,non_leaf_count):
        parentIndex=i
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2

        if leftChildIndex<len(lst):
            if arr[parentIndex]>arr[leftChildIndex]:
                if rightChildIndex<len(lst):
                    if arr[parentIndex]>arr[rightChildIndex]:
                        flag=True
                    else:
                        flag=False
                        break
                else:
                    continue
            else:
                flag=False
                break

    return flag
        

    

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')

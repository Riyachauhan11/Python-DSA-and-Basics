'''You are given an array of unique integers that contain numbers in random order. 
You have to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains starting and ending element. 
If the length of the longest possible sequence is one, then the output array must contain only single element.

Note:
1. Best solution takes O(n) time.
2. If two sequences are of equal length, then return the sequence starting with the number whose occurrence is earlier in the array.

Input format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol n.
The following line contains n space separated integers, that denote the value of the elements of the array.

Output format:
The first and only line of output contains starting and ending element of the longest consecutive sequence. 
If the length of  the longest consecutive sequence is 1, then just print the starting element.

Constraints :
0 <= n <= 10^6
Time Limit: 1 sec

Sample Input 1 :

13
2 12 9 16 10 5 3 20 25 11 1 8 6 

Sample Output 1 :

8 12 

Sample Input 2 :

7
3 7 2 1 9 8 41

Sample Output 2 :

7 9
Explanation: Sequence should be of consecutive numbers. 
Here we have 2 sequences with same length i.e. [1, 2, 3] and [7, 8, 9], 
but we should select [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array 
and therefore, the output will be 7 9, as we have to print starting and ending element of the longest consecutive sequence.

Sample Input 3 :

7
15 24 23 12 19 11 16

Sample Output 3 :

15 16'''

from sys import stdin


class MapNode():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map():

    def __init__(self,n):
        self.bucketSize=n
        self.buckets=[None for i in range(self.bucketSize)]

    def getBucketIndex(self,hc):
        return (abs(hc) % (self.bucketSize))

    def insert(self,key,value):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]

        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        
        head=self.buckets[index]

        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[index]=newNode


    def getValue(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]

        while head is not None:
            if head.key==key:
                return head.value
            head=head.next

        return None
    




def longestConsecutiveSubsequence(arr,n): 
    # Write your code here

   
    visitedElements = {}
    elementToIndexMapping = {}
    for i in range(n):
        elementToIndexMapping[arr[i]] = i
        if arr[i] not in visitedElements:
            visitedElements[arr[i]]=True

    longestSequence=[]
    maxSequenceLength = 1
    minStartIndex = 0

    for i in range(n):
        num = arr[i]
        currentMinStartIndex = i
        count = 0
        tempNum = num
        while tempNum in visitedElements and visitedElements [tempNum]==True:
            visitedElements [tempNum] = False
            count+=1
            tempNum+=1

        tempNum = num - 1
        while tempNum in visitedElements and visitedElements [tempNum]==True:
            visitedElements [tempNum] = False
            count+=1
            currentMinStartIndex = elementToIndexMapping[tempNum]
            tempNum-=1
        if (count > maxSequenceLength):
            maxSequenceLength = count
            minStartIndex = currentMinStartIndex

        elif (count == maxSequenceLength):
            if (currentMinStartIndex < minStartIndex):
                minStartIndex = currentMinStartIndex

    startNum = arr[minStartIndex]
    longestSequence.append(startNum)

    if (maxSequenceLength > 1):
        longestSequence.append(startNum + maxSequenceLength - 1)
    return longestSequence


        


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
if type(ans)==int:
    print(ans)
else:
# This ans array contains two numbers, ie, start and end of longest sequence respectively
    print(*ans)

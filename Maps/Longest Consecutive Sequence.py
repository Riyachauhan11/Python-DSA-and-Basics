'''You are given an array of unique integers that contain numbers in random order. 
You have to find the longest possible sequence of consecutive numbers using the numbers from given array.
You need to return the output array which contains starting and ending element. 
If the length of the longest possible sequence is one, then the output array must contain only single element.

Note:

1. Best solution takes O(n) time.
2. If two sequences are of equal length, then return the sequence starting with the number whose occurrence is earlier in the array.

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
but we should select [7, 8, 9] because the starting point of [7, 8, 9] comes first in input array and therefore, 
the output will be 7 9, as we have to print starting and ending element of the longest consecutive sequence.'''

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

    if len(arr)==0:
        return 0

    maxLength=1
    highest_no=0
    lowest_no=0
    lowest_index=None

    hash_map=Map(n)
    for no in arr:
        hash_map.insert(no,True)
    
    for no in arr:
        #print(lowest_no,highest_no)
        if hash_map.getValue(no)==True:
            count=1
            i=no+1
            j=no-1


            while hash_map.getValue(i)!=None:
                #print(i)
                count+=1
                hash_map.insert(i,False)
                i+=1
            while hash_map.getValue(j)!=None:
                count+=1
                hash_map.insert(j,False)
                j-=1

            if count>maxLength:

                maxLength=count
                highest_no=i-1
                lowest_no=j+1

                if lowest_index==None:
                    lowest_index=arr.index(lowest_no)
            
            elif lowest_index!=None:
                if count==maxLength and arr.index(j+1)<lowest_index:
                    highest_no=i-1
                    lowest_no=j+1

    if lowest_no==0 and highest_no==0:
        return arr[0]



    return lowest_no,highest_no

        


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

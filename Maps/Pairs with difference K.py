'''You are given with an array of integers and an integer K. 
You have to find and print the count of all such pairs which have difference K.
Note: Take absolute difference between the elements of the array.

Sample Input 1 :
4 
5 1 2 4
3

Sample Output 1 :
2

Sample Input 2 :
4
4 4 4 4 
0

Sample Output 2 :
6
'''

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

        return 0


    def remove(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]
        prev=None

        while head is not None:            
            if head.key==key:
                if prev is not None:
                    prev.next=head.next
                else:
                    self.buckets[index]=head.next
                return head.value
            
            prev=head
            head=head.next

        return None



def printPairDiffK(l, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    count=0
    hash_map=Map(n)
    d={}

    for no in l:
        d[no]=d.get(no,0)+1

    for ele in d:
        hash_map.insert(ele,d[ele])

    for num in d:
        if k!=0:
            value=hash_map.getValue(num)
            value1=hash_map.getValue(num-k)
            value2=hash_map.getValue(num+k)

            count=count+value*(value1+value2)

            hash_map.remove(num)
        else:
            sum=0
            l=d[num]-1
            add=d[num]-1
            for i in range(l):
                sum+=add
                add-=1
                
            count+=sum

    return count

    
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))

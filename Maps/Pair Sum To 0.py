'''Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
Note: Array A can contain duplicate elements as well.
  
Sample Input 1:

5
2 1 -2 2 3

Sample Output 1:

2'''

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


    
    
# Main

def pairSum0(l,n):
    count=0
    hash_map=Map(n)
    d={}

    for no in l:
        d[no]=d.get(no,0)+1

    for ele in d:
        hash_map.insert(ele,d[ele])

    for num in d:
        if num!=0:
            value=hash_map.getValue(num)
            value1=hash_map.getValue(-num)

            count=count+value*value1

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


    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))


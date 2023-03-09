'''Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.

Sample Input 1:

10 
 95 -97 -387 -435 -5 -70 897 127 23 284

Sample Output 1:

5

Explanation:

The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 '''

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
                prev_index=head.value
                head.value=value
                return prev_index
            head=head.next
        
        head=self.buckets[index]

        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[index]=newNode
        return None


    def getValue(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]

        while head is not None:
            if head.key==key:
                return head.value
            head=head.next

        return 0



def subsetSum(l):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    maxlength=0
    length=0
    hash_map=Map(len(l))
    index=0
    prev_no=-10000000
    deciding=0

    
    d={}

    sum=0
    sum_arr=[]

    for no in l:
        sum+=no
        sum_arr.append(sum)
    
    for no in sum_arr:
        d[no]=d.get(no,0)+1



    for no in sum_arr:

        if prev_no==no:
            index+=1
            continue

        if no==0:
            length=index+1
            if length>maxlength:
                maxlength=length


        rep=hash_map.insert(no,index)
        if rep!=None:
            length=index-rep
            if length>maxlength:
                maxlength=length
                deciding=no
            elif no==deciding and maxlength+length<=len(l):
                maxlength+=length
        

        index+=1
        prev_no=no

    #print(sum_arr)
    return maxlength



# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))


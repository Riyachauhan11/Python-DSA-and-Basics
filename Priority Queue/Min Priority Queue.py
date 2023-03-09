class PriorityQueueNode():
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class PriorityQueue():
    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childIndex=self.getSize()-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex].priority<self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break

    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        ParentIndex=0
        LeftChildIndex=2*ParentIndex+1
        RightChildIndex=2*ParentIndex+2


        while LeftChildIndex<self.getSize():
            min_index=ParentIndex

            if self.pq[min_index].priority>self.pq[LeftChildIndex].priority:
                min_index=LeftChildIndex            
            if RightChildIndex<self.getSize() and self.pq[min_index].priority>self.pq[RightChildIndex].priority:
                min_index=RightChildIndex

            if min_index==ParentIndex:
                break
            
            self.pq[ParentIndex],self.pq[min_index]=self.pq[min_index],self.pq[ParentIndex]
            ParentIndex=min_index       
            LeftChildIndex=2*ParentIndex+1
            RightChildIndex=2*ParentIndex+2

        
    def removeMin(self):
        ans=self.getMin()
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ans
        
pq=PriorityQueue()
pq.insert('A',10)
pq.insert('B',19)
pq.insert('C',20)
pq.insert('D',5)

for i in range(pq.getSize()):
    print(pq.removeMin())

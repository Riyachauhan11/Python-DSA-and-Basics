'''You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.
A queue is maintained for buying the tickets and every person is attached with a priority (an integer, 1 being the lowest priority).
The tickets are sold in the following manner -

1. The first person (pi) in the queue requests for the ticket.
2. If there is another person present in the queue who has higher priority than pi, then ask pi to move at end of the queue without giving him the ticket.
3. Otherwise, give him the ticket (and don't make him stand in queue again).

Giving a ticket to a person takes exactly 1 second and it takes no time for removing and adding a person to the queue. And you can assume that no new person joins the queue.
Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0). Find and return the time it will take until you get the ticket.
Input Format:

The first line of input contains an integer, that denotes the value of total number of people standing in queue or the size of the array of priorities. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array of priorities.
The following contains an integer, that denotes the value of index of your priority. Let us denote it with symbol k.

Output Format :

The first and only line of output contains the time required for you to get the ticket.

Constraints:

Time Limit: 1 sec

Sample Input 1 :

3
3 9 4
2

Sample Output 1 :

2

Sample Output 1 Explanation :

Person with priority 3 comes out. But there is a person with higher priority than him. 
So he goes and then stands in the queue at the end. Queue's status :  {9, 4, 3}. Time : 0 secs.
Next, the person with priority 9 comes out. And there is no person with higher priority than him. 
So he'll get the ticket. Queue's status :  {4, 3}. Time : 1 secs.
Next, the person with priority 4 comes out (which is you). And there is no person with higher priority than you. So you'll get the ticket. Time : 2 secs.

Sample Input 2 :

5
2 3 2 2 4
3

Sample Output 2 :

4

'''


from sys import stdin
import sys
import heapq as heap

class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data
    
def buyTicket(tickets, n, k) : 
    ######################
    #PLEASE ADD CODE HERE#
    ######################
    q=Queue ()
    #Max priority queue
    maxHeap =[]
    heap.heapify (maxHeap)
    for element in arr :
        q.enqueue (element)
        heap.heappush(maxHeap, -1*element)# Add first k elements to max heap by negating elements, we r using -1 as we r making max heap using min heap func
    count = 0
    while len (maxHeap) != 0 :
        if q.peek()==-1*maxHeap[0] :
            if k == 0:
                return count + 1
            else :
                count += 1
                q.dequeue ()
                heap.heappop (maxHeap)
                k -= 1
        else :
            q.enqueue (q.peek())
            q.dequeue ()
            if k == 0:
                k=q.getSize()-1
            else:
                k-=1
    return count






#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print(buyTicket(arr, n, k))

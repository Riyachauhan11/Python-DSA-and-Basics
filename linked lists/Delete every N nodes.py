'''You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' 
Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. 
Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.'''

'''Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line of input contains two integer values 'M,' and 'N,' respectively. A single space will separate them.'''

'''Remember/Consider :
While specifying the list elements for input, -1 
indicates the end of the singly linked list 
and hence, would never be a list element'''


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def skipMdeleteN(head, M, N) :
	#Your code goes here
    temp=head
    if M==0:
        return None
    while head is not None:
        M2 = M
        N2 = N
        while M2 > 0 and head is not None:
            pointer = head
            head = head.next
            M2-=1
        while N2 > 0 and head is not None:
            head = head.next
            N2-=1
        pointer.next=head
    return temp     


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1

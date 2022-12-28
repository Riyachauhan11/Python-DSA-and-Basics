'''You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.

Note :
Assume that the Indexing for the linked list always starts from 0.

If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.

Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
'''



from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def lengthll(head):
    count=0
    while head is not None:
        if head==-1:
            break
        count+=1
        head=head.next
    return count


def deleteNode(head, pos) :
    # Write your code here.
    length=lengthll(head)
    if pos<0 or pos>=length:
        return head

    prev=None
    curr=head
    count=0

    while count<pos:
        prev=curr
        curr=curr.next
        count+=1

    if prev is not None:
        curr=curr.next
        prev.next = curr
    else:
        head=head.next

    return head


# Taking Input Using Fast I/O.
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

  
# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
    
    
-------------------------------------------------------------------------------------------

# recursively :

def deleteNodeRec(head, pos) :
	#Your code goes here
    if pos<0:
        return head
    if head is None:
        return None
    if pos==0:
        head=head.next
        return head

    small_head=deleteNodeRec(head.next,pos-1)
    head.next=small_head
    return head
    

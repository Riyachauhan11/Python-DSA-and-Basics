'''Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
'k' is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
Example :

Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4'''


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def lengthLL(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count



def kReverse(head, k):

    # Base condition.
    if(head == None):
        return None

    if k==0:
        return head

    curr, prev, ahead = head, None, None
    count = k

    # Reversing the first K nodes.
    while(curr != None and count > 0):
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead
        count -= 1

    # Recursively calling for the remaining list.
    if(curr != None):
        head.next = kReverse(curr, k)

    # Returning the new head.
    return prev




def reverse3(head):
    if head is None or head.next is None:
        return head
    smallhead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead

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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1

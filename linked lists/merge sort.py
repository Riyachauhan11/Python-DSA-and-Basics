'''Given a singly linked list of integers, sort it using 'Merge Sort.'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeSort(head) :
	#Your code goes here
    if head is None or head.next is None:
        return head
    slow =head
    fast=head
    while (fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    #above program gives us midpoint of linked list in slow node
    mid=slow
    head1=head
    head2=mid.next
    mid.next=None
    part_1=mergeSort(head1)
    part_2=mergeSort(head2)
    return merge(part_1,part_2)


# to merge 2 sorted linked lists
def merge(head1,head2):
    if head1 == None and head2 == None:
        return None
    elif head1 != None and head2 == None:
        return head1
    elif head1 == None and head2 != None:
        return head2
    
    final_head=None
    final_tail=None

    if head1.data > head2.data:
        final_head=head2
        final_tail=head2
        head2=head2.next
    else:
        final_head=head1
        final_tail=head1
        head1=head1.next

    while (head1 != None and head2 !=None):
        if head1.data > head2.data:
            final_tail.next=head2
            final_tail=final_tail.next
            head2=head2.next
        else:
            final_tail.next=head1
            final_tail=final_tail.next
            head1=head1.next
    if head1 != None:
        final_tail.next=head1
    else:
        final_tail.next=head2
    return final_head


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

    newHead = mergeSort(head)
    printLinkedList(newHead)
    t -= 1

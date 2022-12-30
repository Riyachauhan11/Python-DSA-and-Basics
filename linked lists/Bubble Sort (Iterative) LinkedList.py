'''Given a singly linked list of integers, sort it using 'Bubble Sort.'''

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def bubbleSort(head) :
    if (head != None) :
        current = None
        status = False
        while True :
            # Start with first node
            current = head
            # Reset working status
            status = False
            while (current != None and current.next != None) :
                if (current.data > current.next.data) :
                    # Swap node values
                    current.data = current.data + current.next.data
                    current.next.data = current.data - current.next.data
                    current.data = current.data - current.next.data
                    # When node value change
                    status = True
                # Visit to next node
                current = current.next
            if((status) == False) :
                    break
    else :
        return head
    return head




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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)

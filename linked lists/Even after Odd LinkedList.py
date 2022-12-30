from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    #Your code goes here
    if head is None:
        return head
    even_node=None
    odd_node=None
    odd_node_head=None
    even_node_head=None
    

    while head is not None:
        if head.data % 2 == 0 and even_node_head==None:
            even_node_head=head
            even_node=head
            head=head.next
        elif head.data %2 != 0 and odd_node_head==None:
            odd_node_head = head
            odd_node=head
            head=head.next

        if head.data % 2 == 0 and even_node_head != None:
            even_node.next = head
            even_node=even_node.next
            head=head.next            
        elif head.data % 2 != 0 and odd_node_head != None:
            odd_node.next = head
            odd_node=odd_node.next
            head=head.next
            

    if even_node_head==None:
        return odd_node_head
    elif odd_node_head==None:
        return even_node_head

    odd_node.next=None
    even_node.next=None

    odd_node.next=even_node_head
    return odd_node_head
        


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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1

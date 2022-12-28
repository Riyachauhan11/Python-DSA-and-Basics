'''You have been given a singly linked list of integers along with an integer 'N'. 
Write a function to append the last 'N' nodes towards the front of the 
singly linked list and returns the new head to the list.'''

'''Sample Input :
2
1 2 3 4 5 -1
3
10 20 30 40 50 60 -1
5

Sample Output :
3 4 5 1 2
20 30 40 50 60 10'''


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def lengthLL(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count


def appendLastNToFirst(head, n) :
    #Your code goes here
    if n==0:
        return head
    temp=head
    length=lengthLL(head)
    pos=length-n
    end_nodes=head
    count=0

    while head is not None:
        if count==pos:
            temp=head
            break
        head=head.next
        count+=1

    while head is not None:
        curr=head
        head=head.next

    for i in range(pos):
        newNode=Node(end_nodes.data)
        curr.next=newNode
        curr=newNode
        end_nodes=end_nodes.next
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
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 

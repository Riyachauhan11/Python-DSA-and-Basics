'''You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' 
(if it exists). Return -1 otherwise.

Note :
Assume that the Indexing for the singly linked list always starts from 0.

Output format :

For each test case, return the index/position of 'N' in the singly linked list. Return -1, otherwise.
Output for every test case will be printed in a separate line.'''

from sys import stdin

# Following is the Node class already written for the Linked List.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthll(head):
    count = 0
    while head is not None:
        if head == -1:
            break
        count += 1
        head = head.next
    return count


def findNode(head, n):
    # Write your code here.
    pos = 0
    while head is not None:
        if head.data == n:
            return pos
        head = head.next
        pos += 1
    return -1



def findNodeRec(head, n) :
	#Your code goes here
    if head == None:
        return -1
    if head.data == n:
        return 0
    index= findNodeRec(head.next,n)
    if index != -1:
        return index+1
    else:
        return -1
    


# Taking Input Using Fast I/O.
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# To print the linked list.
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()







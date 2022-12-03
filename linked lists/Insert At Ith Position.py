class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Take_input():
    arr = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currdata in arr:
        if currdata == -1:
            break

        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


def lengthLL(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def printll(head):
    while head is not None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return


def insert(head, i, data):
    length = lengthLL(head)
    temp = head
    if i >= 0 and i <= length:
        newNode = Node(data)
        prev = i-1
    count = 0
    while count < i:
        if count == prev:
            prev_node = temp
        temp = temp.next
        count += 1
    curr_node = temp
    if prev != -1:
        prev_node.next = newNode
    else:
        head = newNode
    newNode.next = curr_node
    return head
  
  
---------------------------------------------------------------------------------------------------

def insert_at_i(head, i, data):
    length = lengthLL(head)
    count = 0

    if i < 0 or i > length:
        return head

    newNode = Node(data)
    prev = None
    curr = head

    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    return head


ll = Take_input()
printll(ll)
head = insert(ll, 5, 11)
printll(head)

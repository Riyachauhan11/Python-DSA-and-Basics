'''Given a generic tree and an integer n. Find and return the node with next larger element in the tree 
i.e. find a node with value just greater than n.

Note: Return NULL if no node is present with the value greater than n.

Sample Input 1 :

10 3 20 30 40 2 40 50 0 0 0 0 
18

Sample Output 1 :

20
'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree==None:
        return

    next_l=None

    if tree.data>n:
        next_l=tree

    for child in tree.children:
        if next_l !=None:
            if child.data>n and child.data<next_l.data:
                next_l=child
        else:
            if child.data>n:
                next_l=child
                
        value=nextLargest(child,n)
        if value!=None and next_l==None:
            next_l=value

        elif value!=None and next_l!=None:
            if value.data<next_l.data:
                next_l=value

    
    return next_l


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)

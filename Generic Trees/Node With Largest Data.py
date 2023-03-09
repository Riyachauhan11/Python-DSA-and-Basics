'''Given a generic tree, find and return the node with maximum data. You need to return the node which is having maximum data.
Return null if tree is empty.

Sample Input 1:

10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1:

50

'''

import sys
sys.setrecursionlimit(3000)
from sys import stdin
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree==None:
        return
    maximum=tree
    for child in tree.children:
        if child.data>maximum.data:
            maximum=child
        value=maxDataNode(child)
        if value.data>maximum.data:
            maximum=value

    
    return maximum



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
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
print(maxDataNode(tree))

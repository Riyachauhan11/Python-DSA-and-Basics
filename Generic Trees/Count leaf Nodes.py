'''Given a generic tree, count and return the number of leaf nodes present in the given tree.'''

import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(root):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root==None:
        return 0

    count=0

    if len(root.children)==0:
        count+=1
    else:
        for child in root.children:
            count=count+leafNodeCount(child)

    return count

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
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(leafNodeCount(tree))

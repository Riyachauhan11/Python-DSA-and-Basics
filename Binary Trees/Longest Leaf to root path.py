'''Given a binary tree, return the longest path from leaf to root. Longest means, a path which contain maximum number of nodes from leaf to root.

Sample Input 1 :

 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1

Sample Output 1 :

9
3
6
5

'''

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def longestPath(root):
    #Implement Your Code Here
    if (root == None):
        return []
 
    # Recursive call on root.right
    rightvect = longestPath(root.right)
 
    # Recursive call on root.left
    leftvect = longestPath(root.left)
 
    # Compare the size of the two vectors
    # and insert current node accordingly
    if (len(leftvect) > len(rightvect)):
        leftvect.append(root.data)
    else:
        rightvect.append(root.data)
 
    # Return the appropriate vector
    if len(leftvect) > len(rightvect):
        return leftvect
 
    return rightvect
    

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
path = longestPath(root)
for ele in path:
    print(ele)


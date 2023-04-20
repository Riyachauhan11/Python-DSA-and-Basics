'''You are given a Binary Tree of type integer, a target node, and an integer value K.
Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.

Input Format:
The first line of input will contain the node data, all separated by a single space. 
Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

The second line of input contains two integers separated by a single space, representing the value of the target node and K, respectively.


Sample Input 1:

5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
3 1

Sample Output 1:

9
6
'''

import queue
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintDepthK(root, k, d=0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    PrintDepthK(root.left, k, d+1)
    PrintDepthK(root.right, k, d+1)


def NodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root)
        return l

    leftOutput = NodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append((root, "L"))
        return leftOutput

    rightOutput = NodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append((root, "R"))
        return rightOutput

    else:
        return None


def isNodePresent(root, x):
    # Write your code here.
    if root == None:
        return False
    if root.data == x:
        return root
    node_left = isNodePresent(root.left, x)
    node_right = isNodePresent(root.right, x)
    if node_left != False or node_right != False:
        if node_left:
            return node_left
        else:
            return node_right
    else:
        return False


def nodesAtDistanceK(root, node, k, nodeToRootPath):
	#Your code goes here
    if root == None:
        return

    if root.data == node:
        PrintDepthK(root, k)

    left_tree = nodesAtDistanceK(root.left, node, k, nodeToRootPath)
    right_tree = nodesAtDistanceK(root.right, node, k, nodeToRootPath)


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodeToRootPath = NodeToRootPath(root, target)
'''print(nodeToRootPath)
for i in range(1, len(nodeToRootPath)):
    print(nodeToRootPath[i][0].data, nodeToRootPath[i][1])'''
nodesAtDistanceK(root, target, k, nodeToRootPath)
if k == 1:
    print(nodeToRootPath[1][0].data)
if nodeToRootPath != None and k > 1:
    for i in range(1, len(nodeToRootPath)):
        node = nodeToRootPath[i][0]
        #print(node.data)
        if k-i-1<0:
            print(node.data)
            break
        if nodeToRootPath[i][1] == 'R':
            PrintDepthK(node.left, k-i-1)
        else:
            PrintDepthK(node.right, k-i-1)

'''For a given Binary of type integer, find and return the ‘Diameter’.
Diameter of a Tree

The diameter of a tree can be defined as the maximum distance between two leaf nodes.
Here, the distance is measured in terms of the total number of nodes present along the 
path of the two leaf nodes, including both the leaves.'''

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Height:
    def __init__(self):
        self.h=0

def diameterOfBinaryTree(root,height):

    lh=Height()
    rh=Height()

    if root ==None:
        height.h=0
        return 0

    ldiameter= diameterOfBinaryTree(root.left,lh)
    rdiameter=diameterOfBinaryTree(root.right,rh)

    height.h=max(lh.h,rh.h)+1

    return max(lh.h+rh.h+1,max(ldiameter,rdiameter))


# time complexity - O(n)
def diameter(root):
    height= Height()
    return diameterOfBinaryTree(root, height)
  
  
  
def height(root):
  if root==None:
      return 0
  return 1 + max(height(root.left),height(root.right)) 
  
  
  
# time complexity - O(n**2)
def diameter2(root):
    # Your code goes here
    if root==None:
        return 0

    left_ht=height(root.left)
    right_ht=height(root.right)
    

    l_diameter=diameterOfBinaryTree(root.left)
    r_diamter=diameterOfBinaryTree(root.right)
    
    return max(left_ht+right_ht+1,max(l_diameter,r_diamter))





#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
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
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root==None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

print(diameter(root))


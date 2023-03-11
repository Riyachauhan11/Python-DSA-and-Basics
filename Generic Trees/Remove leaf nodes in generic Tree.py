'''Remove all leaf nodes from a given generic Tree. Leaf nodes are those nodes, which don't have any children.
Note : Root will also be a leaf node if it doesn't have any child. You don't need to print the tree, 
just remove all leaf nodes and return the updated root.

Input format :
Line 1 : Elements in level order form separated by space (as per done in class). Order is - `
Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element `

Output Format :
Elements are printed level wise, each level in new line (separated by space)

Sample Input 1 :

10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1 : (Level wise, each level in new line)

10
20'''

## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def areNodesSibling(root, a,b):
    
    if(root == None):
        return False


    if(root.left != None and root.right != None): 
        if(root.left.data == a and root.right.data == b):
            return True
        if(root.left.data == b and root.right.data == a):
            return True
    
    if(areNodesSibling(root.left, a,b)):
        return True
    if(areNodesSibling(root.right, a,b)):
        return True

    return False

def findLevel(root,x,level): 
    
    if(root == None):
        return 0
    
    if(root.data == x):
        return level
    
    # if x is found in left subtree
    lev = findLevel(root.left, x, level + 1)
    if(lev): 
        return lev

    return findLevel(root.right, x, level + 1)

def checkCousins(root,a,b): 
    
    # a and b are the given two nodes
    if(a != b and findLevel(root, a, 1) == findLevel(root, b, 1) and areNodesSibling(root, a,b)==False):
        return True
    else:
        return False


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
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')



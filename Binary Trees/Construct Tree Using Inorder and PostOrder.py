'''For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list, 
create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note:
Assume that the Binary Tree contains only unique elements. 

Input Format:

The first line of input contains an integer N denoting the size of the list/array. It can also be said that N is the total number of nodes the binary tree would have.

The second line of input contains N integers, all separated by a single space. It represents the Postorder-traversal of the binary tree.

The third line of input contains N integers, all separated by a single space. It represents the inorder-traversal of the binary tree.'''

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(postOrder, inOrder, n) :
	#Your code goes here
    if len(postOrder)==0:
        return None
        
    rootData=postOrder[-1]
    root=BinaryTreeNode(rootData)

    for i in range(len(inOrder)):
        if inOrder[i]==rootData:
            inorder_left=inOrder[0:i]
            inorder_right=inOrder[i+1:]
            break

    length_left_subtree = len(inorder_left)
    length_right_subtree = len(inorder_right)

    postorder_left = postOrder[0:length_left_subtree]
    postorder_right=postOrder[length_left_subtree:n-1]

    left_st=buildTree(postorder_left,inorder_left,length_left_subtree)
    right_st=buildTree(postorder_right,inorder_right,length_right_subtree)

    root.left=left_st
    root.right=right_st

    return root




'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)

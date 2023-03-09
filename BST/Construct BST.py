'''Given a sorted integer array A of size n, which contains all unique elements. 
You need to construct a balanced BST from this input array. Return the root of constructed BST.
Note: If array size is even, take first mid as root.

Input format:

The first line of input contains an integer, which denotes the value of n. The following line contains n space separated integers, that denote the values of array.

Output Format:

The first and only line of output contains values of BST nodes, printed in pre order traversal.'''

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################

    if len(lst)==0:
        return None

    mid_index=int((len(lst)-1)/2)
    left_side_array=lst[0:mid_index]
    right_side_array=lst[mid_index+1: ]

    root_node=BinaryTreeNode(lst[mid_index])

    left_node = constructBST(left_side_array)
    right_node=constructBST(right_side_array)

    root_node.left=left_node
    root_node.right=right_node

    return root_node


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)


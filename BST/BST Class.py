'''Implement the BST class which includes following functions -
1. insert -
Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.
2. search
Given an element, find if that is present in BST or not. Return true or false.
3. delete -
Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
4. printTree (recursive) -
Print the BST in in the following format -
For printing a node with data N, you need to follow the exact format -

N:L:x,R:y

where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
There is no space in between.
You need to print all nodes in the recursive format in different lines.'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:    
    def __init__(self):
        self.root = None
        self.numNodes = 0


    def printTreehelper(self,root):
        if root==None:
            return
        print(root.data,end=":")
        if root.left != None:
            print("L:"+str(root.left.data),end=",")
        if root.right != None:
            print("R:"+str(root.right.data),end='')
        print()
        self.printTreehelper(root.left)
        self.printTreehelper(root.right)


    def printTree(self):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        self.printTreehelper(self.root)

    
    def searchHelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True

        if root.data>data:
            return self.searchHelper(root.left,data)
        else:
            return self.searchHelper(root.right,data)


    def search(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        return self.searchHelper(self.root,data)


    def insertHelper(self,root,data):
        if root==None:
            node=BinaryTreeNode(data)
            return node
        
        if root.data>=data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root

        
    def insert(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        self.numNodes+=1
        self.root=self.insertHelper(self.root,data)

    
    def min(self,root):
        if root==None:
            return 10000

        if root.left==None:
            return root.data

        return self.min(root.left)
    

    def deleteHelper(self,root,data):
        if root==None:
            return False,None
        
        if root.data>data:
            deleted,newLeftNode=self.deleteHelper(root.left,data)
            root.left=newLeftNode
            return deleted,root
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        if root.left==None and root.right==None:
            return True,None

        if root.left==None:
            return True,root.right
        if root.right==None:
            return True, root.left
        
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newRightNode=self.deleteHelper(root.right,replacement)
        root.right=newRightNode
        return deleted,root

      
    def delete(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        deleted,newRoot=self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newRoot
        return deleted
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()


#a binary tree is balanced if the difference b/w the height of left tree of a node 
#and right tree of the same node is not greater than 1

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PrintTreeDetailed(root):
    if root==None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data,end=" ")
    print()
    PrintTreeDetailed(root.left)
    PrintTreeDetailed(root.right)


def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None

    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def height(root):
    if root==None:
        return 0
    return 1 + max(height(root.left),height(root.right))


#time complexity - minimum= O(n.logn) , max= O(n**2)
def isBalanced(root):
    if root==None:
        return True
    left_height=height(root.left)
    right_height=height(root.right)

    if left_height-right_height>1 or right_height-left_height>1:
        return False
    
    isLeftBalanced=isBalanced(root.left)
    isRightBalanced=isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False


#time complexity - O(n) -> better soln
def getHeightandCheckBalanced(root):
    if root==None:
        return 0,True
    
    lh,isLeftBalanced=getHeightandCheckBalanced(root.left)
    rh,isRighttBalanced=getHeightandCheckBalanced(root.right)

    h=1+max(lh,rh)

    if lh-rh > 1 or rh-lh>1:
        return h,False

    if isLeftBalanced and isRighttBalanced:
        return h,True
    else:
        return h,False
     
#helper function
def isBalanced2(root):
    h,isrootBalanced=getHeightandCheckBalanced(root)
    return isrootBalanced

root=treeInput()
PrintTreeDetailed(root)
#print(isBalanced(root))
#getHeightandCheckBalanced(root)
print(isBalanced2(root))
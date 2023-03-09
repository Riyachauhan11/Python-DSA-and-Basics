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


def removeLeaves(root):
    if root==None:
        return None
    if root.left ==None and root.right==None:
        return None
    root.left=removeLeaves(root.left)
    root.right=removeLeaves(root.right)

    return root



root=treeInput()
PrintTreeDetailed(root)
root=removeLeaves(root)
PrintTreeDetailed(root)

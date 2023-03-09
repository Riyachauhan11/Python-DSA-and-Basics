import queue

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



def takeLevelWiseTreeInput():
    q=queue.Queue()
    print("enter root: ")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while not (q.empty()):
        current_node=q.get()
        print("enter left child of ",current_node.data)
        leftChildData=int(input())
        if leftChildData != -1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)

        print("enter right child of ",current_node.data)
        rightChildData=int(input())
        if rightChildData != -1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)

    return root


def minTree(root):
    if root==None:
        return 10000
    leftMin=minTree(root.left)
    RightMin=minTree(root.right)
    return min(root.data,leftMin,RightMin)

def maxTree(root):
    if root==None:
        return -10000
    leftMax=maxTree(root.left)
    RightMax=maxTree(root.right)
    return max(root.data,leftMax,RightMax)


#time complexity - O(n.logn) --> min , O(n**2) --> max
def isBst(root):
    if root==None:
        return True
    
    leftMax=maxTree(root.left)
    RightMin=minTree(root.right)

    if root.data > RightMin or root.data <= leftMax:
        return False

    isLeftBST=isBst(root.left)
    isRightBST=isBst(root.right)

    return isLeftBST and isRightBST

#time complexity - O(n)
def isBST2(root):
    if root==None:
        return 10000,-10000,True
    
    leftMin,leftMax,isLeftBST=isBST2(root.left)
    rightMin,rightMax,isRightBST=isBST2(root.right)
    
    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    isTreeBST=True

    if root.data<=leftMax or root.data>rightMin:
        isTreeBST= False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST= False

    return minimum,maximum,isTreeBST

    
def isBST3(root,min_range,max_range):
    if root==None:
        return True

    if root.data < min_range or root.data>max_range:
        return False
    
    isLeftWithinConstraints=isBST3(root.left,min_range,root.data-1)
    isRightWithinConstraints=isBST3(root.right,root.data,max_range)

    return isLeftWithinConstraints and isRightWithinConstraints



root=takeLevelWiseTreeInput()
#PrintTreeDetailed(root)
#print(isBST2(root))
print(isBST3(root,-10000,10000))

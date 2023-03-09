'''You are given a generic tree. You have to replace each node with its depth value. 
You just have to update the data of each node, there is no need to return or print anything.

Sample Input 1:

10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1:

0 
1 1 1 
2 2

'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def replacewithDepth(root):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    replacewithDepth_main(root,0)
    


def replacewithDepth_main(root,depth):
    if root==None:
        return 0

    root.data=depth

    for child in root.children:
        replacewithDepth_main(child,depth+1)





def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
replacewithDepth(tree)
printLevelAtNewLine(tree)

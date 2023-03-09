'''Given a generic tree, find and return the height of given tree.

Sample Input 1:

10 3 20 30 40 2 40 50 0 0 0 0 

Sample Output 1:

3'''

import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root


#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.

def height(root):
    if root==None:
        return 0

    h=0

    for child in root.children:
        ch=height(child)
        h=max(h,ch)

    return h+1

li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(height(root))


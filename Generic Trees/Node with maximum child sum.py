'''Given a generic tree, find and return the node for which sum of its data and data of all its child nodes is maximum. 
In the sum, data of the node and data of its immediate child nodes has to be taken.'''

rom sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(tree):
    if tree==None:
        return 
    
    ans=tree
    sum=tree.data

    for child in tree.children:
        sum=sum+child.data
    
    for child in tree.children:
        node,temp_sum=maxSumNode(child)
        if temp_sum>sum:
            sum=temp_sum
            ans=node
    
    return ans,sum



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

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree)
print(temp.data)

'''Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
Note:

1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
2. E is the number of edges present in graph G.
3. You need to take input in main and create a function which should return all the connected components. 
And then print them in the main, not inside function.

Print different components in new line. And each component should be printed in increasing order (separated by space). 
Order of different components doesn't matter.

Input Format :
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains two space separated integers, that denote that there exists an edge between vertex a and b.

Output Format :
Print different components in new line. 
And each component should be printed in increasing order of vertices (separated by space). 
Order of different components doesn't matter.

Constraints :

0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1

Sample Input 1:
4 2
0 1
2 3

Sample Output 1:
0 1 
2 3 

Sample Input 2:
4 3
0 1
1 3 
0 3

Sample Output 2:
0 1 3 
2'''

import queue

#using adjacency matrix
class Graph():
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    #breadth first search
    def __bfsConnectedCompHelper(self,sv,visited,l):
        q=queue.Queue()
        q.put(sv)
        l.append(sv)
        visited[sv]=True
        while not q.empty():
            curr_vertice=q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[curr_vertice][i]>0 and visited[i]==False:
                    l.append(i)
                    q.put(i)
                    visited[i]=True

    def bfsConnectedComp(self):
        final_list=[]
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i]==False:
                l=[]
                self.__bfsConnectedCompHelper(i,visited,l)
                final_list.append(l)
        return final_list


    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]>0:
            return True
        else:
            return False
        
    #changs the deafult str that gets printed when calling print(g)
    def __str__(self):
        return str(self.adjMatrix)



V_E=(input().split())
vertices=int(V_E[0])
edges=int(V_E[1])
g=Graph(vertices)
for i in range(edges):
    v1_v2=(input().split())
    v1=int(v1_v2[0])
    v2=int(v1_v2[1])
    g.addEdge(v1,v2)
ans=g.bfsConnectedComp()
for li in ans:
    li.sort()
    for no in li:
        print(no,end=' ')
    print()


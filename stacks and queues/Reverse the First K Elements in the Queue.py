'''For a given queue containing all integer data, reverse the first K elements.
You have been required to make the desired change in the input queue itself.


Input Format :

The first line of input would contain two integers N and K, separated by a single space. 
They denote the total number of elements in the queue and the count with which the elements need to be reversed respectively.

The second line of input contains N integers separated by a single space, 
representing the order in which the elements are enqueued into the queue.


Sample Input 1:
5 3
1 2 3 4 5


Sample Output 1:
3 2 1 4 5

'''

from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    #Your code goes here
    if k==0:
        return inputQueue
    data=inputQueue.get()
    reverseKElements(inputQueue,k-1)
    inputQueue.put(data)
    


'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

reverseKElements(qu, k)

len_notRev_elements=qu.qsize() - k
count=0
while count<len_notRev_elements:
    data=qu.get()
    qu.put(data)
    count+=1


while not qu.empty() :
    print(qu.get(), end = " ")

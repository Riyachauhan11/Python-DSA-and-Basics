'''You have been given two stacks that can store integers as the data.
Out of the two given stacks, one is populated and the other one is empty. 
You are required to write a function that reverses the populated stack using the one which is empty.'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	#Your code goes here
	if len(inputStack) <=1:
		return
	
	while len(inputStack) != 1:
		ele=inputStack.pop()
		extraStack.append(ele)
	
	last_ele=inputStack.pop()

	while len(extraStack) != 0:
		ele=extraStack.pop()
		inputStack.append(ele)

	reverseStack(inputStack,extraStack)
	inputStack.append(last_ele)




'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")

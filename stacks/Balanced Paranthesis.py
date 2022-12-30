'''For a given a string expression containing only round brackets or parentheses, 
check if they are balanced or not. Brackets are said to be balanced 
if the bracket which opens last, closes first.

Example:

Expression: (()())
Since all the opening brackets have their corresponding closing brackets, 
we say it is balanced and hence the output will be, 'true'.

You need to return a boolean value indicating whether the expression is balanced or not.'''

'''Sample Input 2 :

()()(()

Sample Output 2 :

false

Explanation to Sample Input 2:

The initial two pairs of brackets are balanced.
But when you see, the opening bracket at the fourth index doesn't have its corresponding closing bracket 
which makes it imbalanced and in turn, making the whole expression imbalanced. Hence the output prints 'false'.'''


from sys import stdin

def isBalanced(string):
    s=[]
    for char in string:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
            
        elif char is '}':
            if(not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
    if(not s):
        return True
    return False
            

#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")


'''For a given expression in the form of a string, find if there exist any redundant brackets or not. 
It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.

Example:

Expression: (a+b)+c
Since there are no needless brackets, hence, the output must be 'false'.

Expression: ((a+b))
The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.

Expression: a+(b)+c 
The expression can be reduced to a+b+c. Hence, the brackets are redundant.'''

from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
	s = []
	for char in expression:
		if char != ')':
			s.append(char)
	while len(s) != 0:
		count=0
		for i in range(len(s),-1,-1):
			if s[-1] != '(':
				s.pop()
				count+=1
			else:
				s.pop()
				break
		if count>1:
			continue		
		else:
			return True
	return False


#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")


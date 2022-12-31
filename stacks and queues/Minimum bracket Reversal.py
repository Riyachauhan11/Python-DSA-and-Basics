'''For a given expression in the form of a string, 
find the minimum number of brackets that can be reversed in order to make the expression balanced. 
The expression will only contain curly brackets.
If the expression can't be balanced, return -1.

Example:

Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced. 
Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket 
and hence will not be able to make the expression balanced and the output will be -1.'''


from sys import stdin

def countBracketReversals(inputString) :
    # Your code goes here
    s = []
    count=0
    for bracket in inputString:
            if bracket == '{':
                s.append(bracket)
            elif len(s) != 0 and bracket == '}' and s[-1]=='{':
                s.pop()
            elif bracket =='}':
                s.append(bracket)

    while s:
        c1=s.pop()
        if len(s)==0:
            return -1
        c2=s.pop()
        if c1==c2:
            count+=1
        else:
            count+=2

    return count
		
        
 



#main
print(countBracketReversals(stdin.readline().strip()))


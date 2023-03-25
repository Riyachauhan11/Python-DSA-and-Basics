'''
i)Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
ii)Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.

Note : The order of strings are not important. Just print different strings in new lines.

Input Format :
Integer n

Output Format :
All possible strings in different lines

Constraints :
1 <= n <= 10^6

Sample Input:
23

Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf'''

#RETURN FUNC
def getString(lastDig):
    if lastDig==2:
        return 'abc'
    elif lastDig==3:
        return 'def'
    elif lastDig==4:
        return 'ghi'
    elif lastDig==5:
        return 'jkl'
    elif lastDig==6:
        return 'mno'
    elif lastDig==7:
        return 'pqrs'
    elif lastDig==8:
        return 'tuv'
    elif lastDig==9:
        return 'wxyz'
    return ""

def keypad(n):
    #Implement Your Code Here
    if n==0:
        l=['']
        return l

    smaller_int=n//10
    lastDig=n%10

    smaller_output=keypad(smaller_int)
    optionsForLastDig=getString(lastDig)
    output=[]


    for s in smaller_output:
        for char in optionsForLastDig :
            add=s+char
            output.append(add)
          

    return output

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
    
    
    
#PRINT FUNC
def getoption(lastDig):
    if lastDig==2:
        return 'abc'
    elif lastDig==3:
        return 'def'
    elif lastDig==4:
        return 'ghi'
    elif lastDig==5:
        return 'jkl'
    elif lastDig==6:
        return 'mno'
    elif lastDig==7:
        return 'pqrs'
    elif lastDig==8:
        return 'tuv'
    elif lastDig==9:
        return 'wxyz'
    return ""

def PrintKeypad(inpu,outputSoFar):
    if inpu==0:
        print(outputSoFar)
        return 
    
    small_number=inpu//10
    lastDigit=inpu%10

    optionsForLastDig=getoption(lastDigit)

    for char in optionsForLastDig:
        newOutput=char+outputSoFar
        PrintKeypad(small_number,newOutput)


string=int(input())
PrintKeypad(string,"")

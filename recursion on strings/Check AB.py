'''Suppose you have a string, S, made up of only 'a's and 'b's. 
Write a recursive function that checks if the string was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'

If all the rules are followed by the given string, return true otherwise return false.'''

def checkAB(s):
    if len(s) == 0:
        return 1
    if s[0] == 'a':
        if len(s[1:]) > 1 and s[1:3] == 'bb':
            return checkAB(s[3:])
        else:
            return checkAB(s[1:])
    else:
        return 0

s = input()
if checkAB(s):
    print('true')
else:
    print('false')
    

# another solution
def check_ab(string):
    l=len(string)
    if l==0:
        return 'true'
    if l==1 and string[0]=='a':
        return 'true'
    if string[0]=='b' and string[0]!=string[1]:
        return 'false'
    if string[0]=='a':
        return check_ab(string[1:])
    elif string[0:2]=='bb':
        return check_ab(string[2:])
    
            
string=input()
if string[0]=='b':
    print('false')
else:
    print(check_ab(string))

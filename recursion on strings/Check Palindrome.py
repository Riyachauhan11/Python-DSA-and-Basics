#Check whether a given String S is a palindrome using recursion. 
#Return true or false.

def check_palindrome(string):
    l=len(string)
    if l==0:
        return string
    small_string_output=check_palindrome(string[1:])
    return small_string_output+string[0]
    
string=input()
reversed_word=check_palindrome(string)
if reversed_word==string:
    print('true')
else:
    print('false')

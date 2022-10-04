#Given a string, determine if it is a palindrome, considering only alphanumeric characters.
from sys import stdin


def isPalindrome(string) :
	# Your code goes here
    i=0
    j=-1
    count=len(string)//2
    for k in range(count):
        if string[i]==string[j]:
            i+=1
            j-=1
        else:
            return False
    return True


#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

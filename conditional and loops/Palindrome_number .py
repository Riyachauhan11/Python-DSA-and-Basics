# to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.

def checkPalindrome(num):
    rev=0
    while num>0:
        dig=num%10
        num=num//10
        rev=rev*10+dig
    return rev
num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome)==num:
	print('true')
else:
	print('false')

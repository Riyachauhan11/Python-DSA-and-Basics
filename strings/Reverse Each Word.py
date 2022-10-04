'''Aadil has been provided with a sentence in the form of a string as a function parameter. 
The task is to implement a function so as to print the sentence such 
that each word in the sentence is reversed.

Example:

Input Sentence: "Hello, I am Aadil!"
The expected output will print, ",olleH I ma !lidaA". '''

from sys import stdin
def reverseEachWord(string) :
	# Your code goes here
    new_str=string[::-1]
    li=new_str.split()
    li=li[::-1]
    final=''
    for i in range(len(li)):
        final=final+li[i]+' '
    return final  


#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)

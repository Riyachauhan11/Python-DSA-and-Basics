'''For a given string(str), remove all the consecutive duplicate characters.
Example:

Input String: "aaaa"
Expected Output: "a"

Input String: "aabbbcc"
Expected Output: "abc" '''

from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
    new_str=''
    i=0
    length=len(string)
    while i<=length-1:
        for j in range(i+1,length):
            if string[i]==string[j]:
                i+=1
            else:
                break
        new_str+=string[i]
        i+=1
    return new_str    
            
        
        

#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)

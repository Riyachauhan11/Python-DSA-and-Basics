'''For a given a string(str), find and return the highest occurring character.

Example:

Input String: "abcdeapapqarr"
Expected Output: 'a'
Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.

If there are two characters in the input string with the same frequency, return the character which comes first.

Consider:
Assume all the characters in the given string to be in lowercase always.'''


from sys import stdin

def highestOccuringChar(string) :
	#Your code goes here
    freq=[]
    for i in range(256):
        freq.append(0)
    for i in range(len(string)):
        val=ord(string[i])
        freq[val]=freq[val]+1
    return chr(freq.index((max(freq))))




#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)

#For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.

#Two strings are said to be a permutation of each other when either of the string's 
#characters can be rearranged so that it becomes identical to the other one.

#Example: 
#str1= "sinrtg" 
#str2 = "string"

#The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.

from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    freq=[]
    freqc=[]
    for i in range(256):
        freq.append(0)
    for i in range(len(string1)):
        val=ord(string1[i])
        freq[val]=freq[val]+1
    for j in range(len(string2)):
        val=ord(string2[j])
        freq[val]=freq[val]-1
    for i in range(256):
        freqc.append(0)
    if freq==freqc:
        return True
    else:
        return False



#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

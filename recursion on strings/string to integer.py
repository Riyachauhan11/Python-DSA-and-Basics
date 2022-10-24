'''Write a recursive function to convert a given string into the number it represents. 
That is input will be a numeric string that contains only numbers, 
you need to convert the string into corresponding integer and return the answer.

Input format :
Numeric string S (string, Eg. "1234")

Output format :
Corresponding integer N (int, Eg. 1234)

Sample Input 1 :
00001231

Sample Output 1 :
1231'''


def string_to_int(string):
    length=len(string)
    if length==1:
        return int(string)
    first_dig=string[0]
    return string_to_int(string[1:])+int(first_dig)*(10**(length-1))


string=input()
print(string_to_int(string))

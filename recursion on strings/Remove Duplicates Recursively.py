# Given a string S, remove consecutive duplicates from it recursively.

def removeConsecutiveDuplicates(string):
    # Please add your code here
    l=len(string)
    if l==0 or l==1:
        return string
    if string[0]==string[1]:
        small_output=removeConsecutiveDuplicates(string[1:])
        return small_output
    else:
        small_output=removeConsecutiveDuplicates(string[1:])
        return string[0]+small_output
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))

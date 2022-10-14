#Given a string, compute recursively a new string where all 'x' chars have been removed.

def removeX(string): 
    if len(string)==0:
        return string
    small_output=removeX(string[1:])
    if string[0]=='x':
        return small_output
    else:
        return string[0]+small_output
    

# Main
string = input()
print(removeX(string))

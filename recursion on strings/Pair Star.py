'''Given a string S, compute recursively a new string where identical chars that are
adjacent in the original string are separated from each other by a "*".'''

def pair_star(string):
    if len(string)==2 and string[0]!=string[1]:
        return string
    elif len(string)==2 and string[0]==string[1]:
        return string[0]+'*'+string[1]
    needed=pair_star(string[1:])
    if string[0]==string[1]:
        return string[0]+'*'+string[1]+needed[1:]
    else:
        return string[0]+needed
            
string=input()
print(pair_star(string))

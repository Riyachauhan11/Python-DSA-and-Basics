#replacing every pi in string with 3.14

def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0] == 'p' and s[1] =='i':
        small_output=replace_pi(s[2:])
        return '3.14'+small_output
    else:
        small_output=replace_pi(s[1:])
        return s[0]+small_output

print(replace_pi('pi2ippi'))

'''note : when dry running the code, make sure to go into the correct if or else block while returning the values to each
call of function.If a function is being called in if block it doesnt exactly mean that the return statement in same if block 
will be ran for that function.'''

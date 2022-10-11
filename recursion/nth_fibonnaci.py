#finding nth fibonacci number

def fib(n):
    if n==1 or n==2:
        return 1
    fib_n_1=fib(n-1)
    fib_n_2=fib(n-2)
    output=fib_n_1+fib_n_2
    return output

print(fib(6))

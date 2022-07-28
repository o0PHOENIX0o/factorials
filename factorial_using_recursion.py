def fact(n):
    if n<=100:
        if n==0 or n==1:
            return 1
        else:
            return n * fact(n-1)
    else:
        return ('try smaller number')
a=int(input('enter a no. '))
print(fact(a))
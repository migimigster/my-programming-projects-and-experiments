def sumBy3(n,x=0):
    if n<=1:
        return x
    else:
        return sumBy3(n-3,x+n)

print(sumBy3(92))
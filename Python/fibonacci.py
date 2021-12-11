import statistics
def fibo(n):
    a=0
    b=1
    arr=[]
    if n==1:
        print(a)
    else:
        arr.append(a)
        arr.append(b)
        for i in range (0,n):
            c=a+b
            a=b
            b=c
            arr.append(c)
        print(arr)


fibo(10)
def  fib(n):
    a,b,s=0,1,0
    while s<n:
        a,b =b,a+b  #  a=0,b=1,c=a,a=b,b=c+b
        s =s+1
        #print(b)
        yield(b) #yield 在python2 里是对象生成器

fib(5)
m =fib(5)
m.next   




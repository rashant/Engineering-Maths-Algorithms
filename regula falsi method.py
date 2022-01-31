from math import *
c=2
d=3
eq='x*log10(x)-1.2'
lis=[]
i=1
it=2
while True:
    print()
    print('iteration:- ',i)
    a=x=c
    print('a=',a)
    fa=eval(eq)
    fa=round(fa,6)
    print('f(a)=',fa)
    b=x=d
    print('b=',b)
    fb=eval(eq)
    fb=round(fb,6)
    print('f(b)=', fb)
    if fa*fb<0:
        x=(a-(((b-a)/(fb-fa))*fa))
        x=round(x,5)
        lis.append(x)
        print(f'x{it}=',x)
    fx=eval(eq)
    fx=round(fx,6)
    print('f(x)=', fx)
    if i>1:
        difference=round((round(lis[i-1],4))-round(lis[i-2],4),4)
        print('difference:-',abs(difference))
        if round(difference,3)==0.000:
            break
    if fx*fb<0:
        c=x
        d=b
    else:
        c=a
        d=x
    i=i+1
    it+=1
print('\n******************************************************************')
print('the accurate root is:- ',x)
print('******************************************************************')

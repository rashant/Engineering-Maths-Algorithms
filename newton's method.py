from sympy import *
from math import *
import pandas as pd
x=symbols('x')
exp= ' x**3-2*x-5'
exp_diff = (Derivative(exp, x)).doit()
exp_diff=str(exp_diff)
c=2
d=3
xlis=[d]
difflis=[]
i=1
it=2
while True:
    print()
    print('iteration:- ',i)
    x=xlis[i-1]
    y=xlis[i-1]-(eval(exp)/eval(exp_diff))
    y = round(y, 4)
    xlis.append(y)
    print(xlis[i-1],eval(exp),eval(exp_diff))
    print(f'x{i+1}= ',y)
    if i>1:
        difference=round((round(xlis[i],4))-round(xlis[i-1],4),4)
        print('difference:-',abs(difference))
        if round(difference,3)==0.000:
            break
    i+=1

print('\n******************************************************************')
print('the accurate root is:- ',y)
print('******************************************************************')
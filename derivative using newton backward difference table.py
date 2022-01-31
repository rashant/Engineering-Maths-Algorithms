import pandas as pd
import math
x=[0,5,10,15,20]
h=x[1]-x[0]
x_values=x
y=[0,3,14,69,228]
y_values=y
y_not=[]
y_n=[]
a=[]
for i in range(len(x)):
    if i<len(x):
        a.append(x[i])
        a.append(' ')
a.pop()
b=[]
for i in range(len(x)):
    if i<len(x):
        b.append(y[i])
        b.append(' ')
b.pop()

df=pd.DataFrame({'X': a, 'Y': b})

fir_dif = []
j=1
z=len(y)
data=[]
while j<z:
    lisz=[]
    for i in range((len(y)-1)):
        fir_dif.append(round(y[i+1]-y[i],4))
    y=fir_dif
    y_not.append(y[0])
    y_n.append(y[len(y)-1])
    for _ in range(j):
        lisz.append(' ')
    for k in y:
        lisz.append(k)
    zx = []
    for o in range(len(lisz)):
        if isinstance(lisz[o], float) or isinstance(lisz[o],int):
            zx.append(lisz[o])
            zx.append(' ')
        else:
            zx.append(lisz[o])
    zx.pop()
    lisz = zx
    for _ in range(j):
        lisz.append(' ')
    df[f'del{j}']=lisz
    fir_dif=[]
    j+=1

x=[]
for i in range(1,len(y_not)+1):
    xy=[]
    for j in range(0,i):
        xy.append(f'(u-{j})')
    z='*'.join(xy)+f'/{math.factorial(i)}'
    x.append(z)
print('***************************************************************************************************************************************')
print('                                                    Difference Table                                                                   ')
print('***************************************************************************************************************************************')
print(df)
print('=======================================================================================================================================\n\n')
eq_term=[]
j=1
for i in range(len(y_not)):
    term = f'((1/{j})*{y_not[i]})'
    j+=1
    eq_term.append(term)
eq=''
for i in range(len(y_not)):
    if i==0:
        eq=eq_term[i]
    elif i>0:
        if i%2!=0:
            eq+=' - '+eq_term[i]
        else:
            eq+= ' + '+eq_term[i]
print('***************************************************************************************************************************************')
print('                                                    eqation                                                                   ')
print('***************************************************************************************************************************************')
eq=f'(1/{h})*( {eq} )'
print('Equation:- '+eq)
print('Answer:- '+str(eval(eq)))
import pandas as pd
import math
x=[5,7,11,13,17]
x_values=x
y=[150,392,1452,2366,5202]
y_values=y
y_not=[]
a=[]
for i in range(len(x)):
    if i<len(x):
        a.append(x[i])
        a.append('')
a.pop()
b=[]
for i in range(len(x)):
    if i<len(x):
        b.append(y[i])
        b.append('')
b.pop()

df=pd.DataFrame({'X': a, 'Y': b})

fir_dif = []
j=1
z=len(y)
data=[]
while j<z:
    lisz=[]
    for i in range((len(y)-1)):
        print(i,j)
        fir_dif.append(round((y[i+1]-y[i])/(x_values[i+j]-x_values[i]),2))
    y=fir_dif
    y_not.append(y[0])
    for _ in range(j):
        lisz.append('')
    for k in y:
        lisz.append(k)
    zx = []
    for o in range(len(lisz)):
        if isinstance(lisz[o], float):
            zx.append(lisz[o])
            zx.append('')
        else:
            zx.append(lisz[o])
    zx.pop()
    lisz = zx
    for _ in range(j):
        lisz.append('')
    df[f'del{j}']=lisz
    fir_dif=[]
    j+=1
x=[]
for i in range(1,len(y_not)+1):
    xy=[]
    for j in range(0,i):
        xy.append(f'(u-{x_values[j]})')
    z='*'.join(xy)
    x.append(z)
print('***************************************************************************************************************************************')
print('                                                    Difference Table                                                                   ')
print('***************************************************************************************************************************************')
print(df)
print('=======================================================================================================================================\n\n')
eq_list_forward=[]
for i in range(len(y_not)):
    term=f'({y_not[i]}*{x[i]})'
    eq_list_forward.append(term)
eq=' + '.join(eq_list_forward)
finaleq=str(y_values[0])+' + '+eq
print('\n\n\n\n*******************************************************************************************************************************************************************************************************************')
print("                                                  Newton's Divided Equation                                                                          ")
print('*******************************************************************************************************************************************************************************************************************')
print(finaleq)
print('*******************************************************************************************************************************************************************************************************************')
u=9
sol=eval(finaleq)
print('\n**********************************************************************************************************************************************************************************************************************************************************')
print(f'U= {u}')
finaleq=finaleq.replace('u',str(u))
print(finaleq)
print(f'At {u}= {round(sol,2)}')
print('**********************************************************************************************************************************************************************************************************************************************************')
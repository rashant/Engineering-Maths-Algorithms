import numpy as np
import pandas
x=[1.0,1.5,2.0,2.5,3.0,3.5,4.0]
y=[1.1,1.3,1.6,2.0,2.7,3.4,4.1]
sigmay=sum(y)
sigmax=sum(x)
n=len(x)
xsquare=[]
for i in x:
    xsquare.append(i*i)
sigmaxsquare=sum(xsquare)
xy=[]
for i in range(len(x)):
    xy.append(x[i]*y[i])
sigmaxy=sum(xy)
xcube=[]
for i in x:
    xcube.append(i*i*i)
sigmaxcube=sum(xcube)
xfour=[]
for i in x:
    xfour.append(i*i*i*i)
sigmaxfour=sum(xfour)
xsquarey=[]
for i in range(len(x)):
    xsquarey.append(x[i]*x[i]*y[i])
sigmaxsquarey=sum(xsquarey)
eq1=f'{n}a + b{sigmax} + c{sigmaxsquare} = {sigmay}'
eq2=f'{sigmax}a + b{sigmaxsquare} + c{sigmaxcube} = {sigmaxy}'
eq3=f'{sigmaxsquare}a + b{sigmaxcube} + c{sigmaxfour} = {sigmaxsquarey}'
x.append('Total')
y.append(sigmay)
xy.append(sigmaxy)
xsquare.append(sigmaxsquare)
xsquarey.append(sigmaxsquarey)
xcube.append(sigmaxcube)
xfour.append(sigmaxfour)
df=pandas.DataFrame({'X': x,'Y':y,'XY':xy,'X²':xsquare,'X²Y':xsquarey,'X³':xcube,'X⁴':xfour})
print(df)
print()
print(eq1)
print(eq2)
print(eq3)
print()
xy_list1=[]
xy_list1.append(n)
xy_list1.append(sigmax)
xy_list1.append(sigmaxsquare)
xy_list2=[]
xy_list2.append(sigmax)
xy_list2.append(sigmaxsquare)
xy_list2.append(sigmaxcube)
xy_list3=[]
xy_list3.append(sigmaxsquare)
xy_list3.append(sigmaxcube)
xy_list3.append(sigmaxfour)
xylist=[xy_list1,xy_list2,xy_list3]

A=np.array(xylist)
inv_A=np.linalg.inv(A)
coff=[]
coff.append(sigmay)
coff.append(sigmaxy)
coff.append(sigmaxsquarey)
B=np.array(coff)
X=np.linalg.inv(A).dot(B)
x1=round(X[0],2)
x2=round(X[1],2)
x3=round(X[2],2)
final_eq=f'{x1}+{x2}*x+{x3}*x**2'
print()
print(final_eq)
x=eval(input('Enter value of x to find the value of y:- '))
print(round(eval(final_eq),2))
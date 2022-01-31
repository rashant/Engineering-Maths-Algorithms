import numpy as np
x=[50,70,100,120]
y=[12,15,21,25]
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
eq1=f'{n}a + b{sigmax} = {sigmay}'
eq2=f'{sigmax}a + b{sigmaxsquare} = {sigmaxy}'
print(eq1)
print(eq2)
xy_list1=[]
xy_list1.append(n)
xy_list1.append(sigmax)
xy_list2=[]
xy_list2.append(sigmax)
xy_list2.append(sigmaxsquare)
xylist=[xy_list1,xy_list2]
print(xylist)
A=np.array(xylist)
inv_A=np.linalg.inv(A)
coff=[]
coff.append(sigmay)
coff.append(sigmaxy)
B=np.array(coff)
X=np.linalg.inv(A).dot(B)
x1=round(X[0],2)
x2=round(X[1],2)
final_eq=f'{x1}+{x2}*x'
x=150
print(eval(final_eq))


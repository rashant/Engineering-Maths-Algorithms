from math import *
import pandas as pd
eq1='(110-y-z)/54'
eq2='(72-2*x-6*z)/15'
eq3='(85+x-6*y)/27'
c=0
d=0
e=0
xlis=[]
ylis=[]
zlis=[]
i=1
while True:
    x=c
    y=d
    z=e
    x1=eval(eq1)
    x,z=x1,e
    y1=eval(eq2)
    x,y=x1,y1
    z1=eval(eq3)
    x1=round(x1,4)
    y1=round(y1,4)
    z1=round(z1,4)
    xlis.append(x1)
    ylis.append(y1)
    zlis.append(z1)
    c=x1
    d=y1
    e=z1
    if i>1:
        diffx=(xlis[i-1]-xlis[i-2])
        diffy=(ylis[i-1]-ylis[i-2])
        diffz=(zlis[i-1]-zlis[i-2])
        if diffx==0.0000 and diffy==0.0000 and diffz==0.0000:
            break
    i+=1
data={'X':xlis,'Y':ylis,'Z':zlis}
df=pd.DataFrame(data)
print(df)

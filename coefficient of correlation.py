import pandas as pd
import math
x=[100,102,104,107,105,112,103,99]
y=[15,12,13,11,12,12,19,26]
a1=x[(int(len(x)/2)+1)]
a2=y[(int(len(y)/2)+1)]
dx=[]
dxsquare=[]
dy=[]
dysquare=[]
for i in x:
    dx.append(i-a1)
for i in dx:
    dxsquare.append(i*i)
for i in y:
    dy.append(i-a2)
for i in dy:
    dysquare.append(i*i)
dxdy=[]
for i in range(len(dx)):
    dxdy.append(dx[i]*dy[i])
sigmadx=sum(dx)
sigmady=sum(dy)
sigmadxdy=sum(dxdy)
sigmadxsquare=sum(dxsquare)
sigmadysquare=sum(dysquare)
x.append('-')
y.append('-')
dx.append(sigmadx)
dy.append(sigmady)
dxdy.append(sigmadxdy)
dxsquare.append(sigmadxsquare)
dysquare.append(sigmadysquare)
df=pd.DataFrame({'X':x,'Y':y,'dX':dx,'dY':dy,'dXdY':dxdy,'dx²':dxsquare,'dy²':dysquare})
r=round(((len(x)*sigmadxdy)-(sigmadx*sigmady))/((math.sqrt((len(x)*(sigmadxsquare)-sigmadx**2)))*(math.sqrt((len(x)*(sigmadysquare)-sigmady**2)))),3)
print(df)
print()
print(r)
if r>0:
    if r>0.50:
        print('strong positive correlation')
    elif r==0.50:
        print('moderate positive correlation')
    else:
        print('weak positive correlation')
elif r==0:
    print('no correlation')
else:
    if r<-0.50:
        print('strong negative correlation')
    elif r==-0.50:
        print('moderate negative correlation')
    else:
        print('weak negative correlation')
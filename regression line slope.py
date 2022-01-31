import pandas as pd
x=[100,102,104,107,105,112,103,99]
y=[15,12,13,11,12,12,19,26]
#a1=x[(int(len(x)/2)+1)]
a1=105
a2=15
#a2=y[(int(len(y)/2)+1)]
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
r=round((sigmadxdy-((sigmadx*sigmady)/len(x)))/(sigmadxsquare-((sigmadx)**2)/len(x)),4)
print(df)
print()
print(r)
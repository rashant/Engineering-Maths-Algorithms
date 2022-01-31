import math
import pandas
print('***************************************************************************************************************************************')
print('                                                    Mean deviation                                                                   ')
print('***************************************************************************************************************************************')

x=[5,15,25,35,45,55,65,75]
f=[5,10,20,40,30,20,10,5]
xf=[]
for i in range(len(x)):
    xf.append(x[i]*f[i])
sigmaxf=sum(xf)
sigmaf=sum(f)
mean=math.floor(sigmaxf/sigmaf)

x_m=[]
for i in range(len(x)):
    x_m.append(abs(x[i]-mean))
fxm=[]
for i in range(len(x)):
    fxm.append(x_m[i]*f[i])
fxm_sum=sum(fxm)
deviation=round(fxm_sum/sigmaf,2)
df=pandas.DataFrame({'X': x, 'f': f,'xf':xf,f'|x-{mean}|':x_m,f'f|x-{mean}|':fxm})
print(df)
print('sigmaf= ',sigmaf)
print('sigmaxf= ',sigmaxf)
print('sigma fx-mean= ',fxm_sum)
print('mean= ',mean)
print('deviation= ',deviation)
print()
print('***************************************************************************************************************************************')
print('                                                    standard deviation                                                                   ')
print('***************************************************************************************************************************************')
xf=[]
for i in range(len(x)):
    xf.append(x[i]*f[i])
sigmaxf=sum(xf)
sigmaf=sum(f)
mean=round(sigmaxf/sigmaf,2)

x_m=[]
for i in range(len(x)):
    x_m.append((x[i]-mean)**2)
fxm=[]
for i in range(len(x)):
    fxm.append(x_m[i]*f[i])
fxm_sum=sum(fxm)
deviation=round((fxm_sum/sigmaf)**(0.5),2)
df=pandas.DataFrame({'X': x, 'f': f,'xf':xf,f'|x-{mean}|':x_m,f'f(x-{mean})^2':fxm})
print(df)
print('sigmaf= ',sigmaf)
print('sigmaxf= ',sigmaxf)
print('sigma fx-mean square= ',fxm_sum)
print('mean= ',mean)
print('deviation= ',deviation)

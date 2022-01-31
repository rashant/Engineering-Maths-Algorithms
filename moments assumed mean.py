import pandas
x=[0 ,1 ,2, 3 ,4 ,5, 6, 7, 8]
f=[1 ,8 ,28, 56 ,70, 56, 28, 8, 1]
x_dup=x
f_dup=f
mid=int(len(x_dup)/2)
a=x_dup[mid]
d=[]
for i in range(len(x_dup)):
    d.append(x_dup[i]-a)
dfv=[]
for i in range(len(x_dup)):
    dfv.append((d[i]*f_dup[i]))
d1=[]
for i in range(len(x_dup)):
    d1.append((x_dup[i]-a)**2)
dfv1=[]
for i in range(len(x_dup)):
    dfv1.append((d1[i]*f_dup[i]))
d2=[]
for i in range(len(x_dup)):
    d2.append((x_dup[i]-a)**3)
dfv2=[]
for i in range(len(x_dup)):
    dfv2.append((d2[i]*f_dup[i]))
d3=[]
for i in range(len(x_dup)):
    d3.append((x_dup[i]-a)**4)
dfv3=[]
for i in range(len(x_dup)):
    dfv3.append((d3[i]*f_dup[i]))
df=pandas.DataFrame({'x':x_dup,'f':f_dup,'d':d,'df1':dfv,'df2':dfv1,'df3':dfv2,'df4':dfv3})
print(df)
a_mean=a+(dfv[-1]/f[-1])
print(f'Mean= {a} + {dfv[-1]}/{f_dup[-1]}')
print(a_mean)
print('First moment about  assumed mean',round(sum(dfv)/sum(f)))
print('second moment about assunmed mean',round(sum(dfv1)/sum(f)))
print('third moment about assumed mean',round(sum(dfv2)/sum(f)))
print('fourth moment about assumed mean',round(sum(dfv3)/sum(f)))

x_dup=x
f_dup=f
mid=int(len(x_dup)/2)
a=a_mean
d=[]
for i in range(len(x_dup)):
    d.append(x_dup[i]-a)
dfv=[]
for i in range(len(x_dup)):
    dfv.append((d[i]*f_dup[i]))
d1=[]
for i in range(len(x_dup)):
    d1.append((x_dup[i]-a)**2)
dfv1=[]
for i in range(len(x_dup)):
    dfv1.append((d1[i]*f_dup[i]))
d2=[]
for i in range(len(x_dup)):
    d2.append((x_dup[i]-a)**3)
dfv2=[]
for i in range(len(x_dup)):
    dfv2.append((d2[i]*f_dup[i]))
d3=[]
for i in range(len(x_dup)):
    d3.append((x_dup[i]-a)**4)
dfv3=[]
for i in range(len(x_dup)):
    dfv3.append((d3[i]*f_dup[i]))
df=pandas.DataFrame({'x':x_dup,'f':f_dup,'d':d,'df1':dfv,'df2':dfv1,'df3':dfv2,'df4':dfv3})
print(df)
print('First moment about  assumed mean',round(sum(dfv)/sum(f)))
print('second moment about assunmed mean',round(sum(dfv1)/sum(f)))
print('third moment about assumed mean',round(sum(dfv2)/sum(f)))
print('fourth moment about assumed mean',round(sum(dfv3)/sum(f)))
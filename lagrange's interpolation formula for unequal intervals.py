import pandas as pd
x=[5,7,11,13,17]
y=[150,392,1452,2366,5202]
formula_term=[]
upper_term=[]
lower_term=[]
numerator = []
denominator = []
df=pd.DataFrame({'X': x, 'Y': y})
print(df)
for i in range(len(x)):
    term=[]
    termx=[]

    for j in range(len(y)):
        if i==j:
            pass
        else:
            zxc=''.join(f'(x-x{j})')
            z=''.join(f'(x{i}-x{j})')
            term.append(zxc)
            termx.append(z)
    zx='*'.join(term)
    zy='*'.join(termx)
    numerator.append(zx)
    denominator.append(zy)

for a in range(len(numerator)):
    formula_term.append(f'({y[a]}*(({numerator[a]})/({denominator[a]})))')
formula=' + '.join(formula_term)
print('\n******************************************************************************************************************************************************************************************')
print('                                                               Equation                                                                    ')
print('********************************************************************************************************************************************************************************************')
print(formula)
print('********************************************************************************************************************************************************************************************')
i,j=0,0
zxc,zx,zy='','',''
numerator,denominator,formula_term=[],[],[]
for i in range(len(x)):
    term=[]
    termx=[]

    for j in range(len(y)):
        if i==j:
            pass
        else:
            zxc=''.join(f'(x-{x[j]})')
            z=''.join(f'({x[i]}-{x[j]})')
            term.append(zxc)
            termx.append(z)
    zx='*'.join(term)
    zy='*'.join(termx)
    numerator.append(zx)
    denominator.append(zy)
a=0
formula=''
for a in range(len(numerator)):
    formula_term.append(f'({y[a]}*(({numerator[a]})/({denominator[a]})))')
formula=' + '.join(formula_term)
print('\n\n************************************************************************************************************************************************************************************')
print(formula)
print('*******************************************************************************************************************************************************************************')

x=9
print('\n\n*************************************************************************************************************************************************')
print('Answer:- ',round(eval(formula),2))
print('*************************************************************************************************************************************************')
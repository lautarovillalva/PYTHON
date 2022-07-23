numero=int(input('ingresar numero: '))

div=0
if(numero>1):
    for i in range(numero+1):
        if(i==0):
            continue
        if(numero%i==0):
            div=div+1
else:
    print(numero, 'no es mayor a 1')

if(div==2):
    print(numero, 'es primo')
else:
    print(numero, 'no es primo')
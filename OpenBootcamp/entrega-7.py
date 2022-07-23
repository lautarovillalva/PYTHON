a=int(input('numero A: '))
b=int(input('numero B: '))

if a <b:
    numero_inicial=a
    numero_final=b
else:
    numero_inicial=b
    numero_final=a


print('los numeros impares entre',numero_inicial,'y',numero_final, 'son:')

for i in range(numero_inicial,numero_final+1):
    if(i%2!=0):
        print(i)

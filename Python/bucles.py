#for
for i in range(5):
    print(i)
    
for i in range(3,5):
    print(i)
    
for i in range(3,20,3):
    print(i)
    
saludos=['hola','adios','hello','bye']
for saludo in saludos:
    print(saludo)

saludos1={
    's0':'hola',
    's1':'hello',
    's2':'hi'
}
for saludo in saludos1.keys():
    print(saludo)
for saludo in saludos1.values():
    print(saludo)
    
#while
q=0
while q<=10:
    print(q)
    q+=1
    if(q==90):
        break
else:
    print('fin del bucle! solo si no entra al break')


    
#condicionales
nums={'numero1':939,
      'numero2':3399}
print(nums)

if(nums['numero1']>nums['numero2']):
    print('numero1 es mayor que numero2')
elif(nums['numero1']==nums['numero2']):
    print('numero2 es igual numero1')
else:
    print('numero2 es mayor que numero1')

if(99 in nums.values()):
    print('está el valor')
    
if('numero1' in nums.keys()):
    print('está la clave')
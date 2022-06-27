from logging import exception


try:
    c=34-3
    print(c)
except ValueError:
    print('s no es un  numero')
except ZeroDivisionError:
    print('no se puede dividir por cero')
except:
    print('error desconocido')
else:
    print('salio todo bien!, voy a ejecutar si no hay errores')


try:
    c=34/0
    print(c)
except ValueError:
    print('s no es un  numero')
except ZeroDivisionError:
    print('no se puede dividir por cero')
except:
    print('error desconocido')
finally:
    print('voy a ejecutar por mas que haya errores')
    
try:
    a=4/0
except Exception as e:
    print(e)
    
b=-4
if(b<0):
    print(b)
    raise Exception('b es menor a cero.')
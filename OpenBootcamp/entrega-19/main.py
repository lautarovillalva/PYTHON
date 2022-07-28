from functools import reduce


def impar(num):
    if num%2!=0:
        return True
    else:
        return False

def sumar(a,b):
    return a+b

def main():
    numeros=[]
    while True:
        numero= int(input('ingresar numero entero, 0 para terminar: '))
        if numero!=0:
            numeros.append(numero)
        else:
            break
    numeros_impares=list(filter(impar, numeros))
    print(list(numeros_impares))
    suma= reduce(sumar, numeros_impares)
    print(suma)

if __name__=='__main__':
    main()
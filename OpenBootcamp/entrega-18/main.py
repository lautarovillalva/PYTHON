def main():
    paises=[]
    while True:
        pais=input('ingresar pais; 0 para terminar: ')
        if pais=='0':
            break
        else:
            paises.append(pais)
    
    paises_ordenados= sorted(paises)

    print(paises_ordenados)


if __name__=='__main__':
    main()
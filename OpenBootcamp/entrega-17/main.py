from entidades.Vehiculo import Vehiculo

def main():
    v1= Vehiculo('Bora', 'Volkswagen', 5)
    with open('entrega-17/fichero.txt','w') as f:
        f.write(str(v1))
    
if __name__=='__main__':
    main()
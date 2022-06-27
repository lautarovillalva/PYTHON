#numéricos

#enteros
from operator import contains


a=1;b=2;c=9;d=9999;
print(a,b,c,d)

#decimales
a=3.14;b=33.2;c=9.5445;d=12321.1232131;
print(a,b,c,d)

#texto
a='Hola mundo!';b="Lautaro Javier Villalva";c='40130286';
print(a,b,c,d)

#booleanos
a=True;b=False;
print(a,b)

#estructuras de datos

#listas
saludos=['hola','hello','hi','chau','goodbye','bye']
saludos.insert(0,'adiós'); saludos.append('buenas tardes')
saludos.remove('hola'); del saludos[1]
print(saludos,
      saludos[0:2],
      saludos[-0],saludos[2],
      print(sorted(saludos))
)

#diccionarios
saludos1={
    's0':'hola',
    's1':'hello',
    's2':'hi'
}
del saludos1['s0']
saludos1['s3']='good bye'
print(saludos1.keys(),
      saludos1.values(),
      len(saludos1),
      's3' in saludos1
)


#tuplas
meses=('ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic')
print(meses)

#conjuntos
contador={3,2,1}
contador.add(0)
print(contador)


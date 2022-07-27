class Vehiculo():
    def __init__(self,modelo, puertas, marca):
        self.modelo=modelo
        self.puertas=puertas
        self.marca=marca

    def __str__(self):
        return f'modelo:{self.modelo}; marca:{self.marca}; cant puertas:{self.puertas}'
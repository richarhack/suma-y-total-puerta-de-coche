class Coche:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas

    def incrementar_puertas(self):
        self.num_puertas += 1

if __name__ == '__main__':
    num_puertas = int(input("¿Cuántas puertas quieres que tenga el coche? "))
    miCoche = Coche(num_puertas)
    print("Mi coche tiene", miCoche.num_puertas, "puertas.")


class Robot:
    def __init__(self, nombre, bateria, escudo):
        self.nombre = nombre
        self.bateria = bateria
        self.escudo = escudo

    def mostrar_estado(self):
        print(f"{self.nombre} -> Batería: {self.bateria}, Escudo: {self.escudo}")

class RobotAtaque(Robot):
    def atacar(self, objetivo):
        if self.bateria >= 10:
            daño = 15
            objetivo.escudo -= daño
            self.bateria -= 10
            print(f"{self.nombre} ataca a {objetivo.nombre} causando {daño} de daño.")
        else:
            print(f"{self.nombre} no tiene suficiente batería para atacar.")

class RobotDefensa(Robot):
    def recargar(self):
        aumento = 20
        self.escudo += aumento
        print(f"{self.nombre} recarga su escudo en {aumento} puntos.")


robot1 = RobotAtaque("Destructor", 100, 50)
robot2 = RobotDefensa("Protector", 80, 60)

robot1.mostrar_estado()
robot2.mostrar_estado()

print("\n--- Turno de ataque ---")
robot1.atacar(robot2)

print("\n--- Estado después del ataque ---")
robot2.mostrar_estado()

print("\n--- Turno de defensa ---")
robot2.recargar()

print("\n--- Turno de ataque ---")
robot1.atacar(robot2)

print("\n--- Estado después del ataque ---")
robot2.mostrar_estado()

print("\n--- Turno de defensa ---")
robot2.recargar()

print("\n--- Estado final ---")
robot2.mostrar_estado()

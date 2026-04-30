from clases import robot
from clases import RobotAtaque
from clases import RobotDefesa
import random

money = 250
robots = []

def menu():
    print(f"Saldo: ${money}")
    print()
    print("¿Que deseas hacer?")
    print("1. Comprar robot")
    print("2. Vender robot")
    print("3. Ver robots")
    print("4. Luchar")
    print("5. Salir")
    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == "1":
        comprar_robot()
    elif opcion == "2":
        vender_robot()
    elif opcion == "3":
        ver_robots()
    elif opcion == "4":
        luchar()
    elif opcion == "5":
        print("Gracias por jugar!")
        exit()
    else:
        print("Opcion no valida")
        menu()



def comprar_robot():
    global money
    print("¿Que tipo de robot quieres comprar?")
    print("1. Robot de ataque - $50")
    print("2. Robot de defensa - $75")
    print("3. Volver al menu")
    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == "1":
        if money >= 5:
            money -= 50
            nombre = input("Ingrese el nombre del robot: ")
            robot_ataque = RobotAtaque()
            robot_ataque.setName(nombre)
            robot_ataque.set_shield(0)
            robot_ataque.set_batery(random.randint(60, 100))
            robots.append(robot_ataque)
            print("Robot de ataque comprado!")
    elif opcion == "2":
        if money >= 50:
            money -= 50
            nombre = input("Ingrese el nombre del robot: ")
            robot_defesa = RobotDefesa()
            robot_defesa.setName(nombre)
            robot_defesa.set_shield(random.randint(40, 80))
            robot_defesa.set_batery(random.randint(80, 100))
            robots.append(robot_defesa)
            print("Robot de defensa comprado!")
    elif opcion == "3":
        menu()
    else:
        print("Opcion no valida")
        comprar_robot()
    menu()

def vender_robot():
    global money
    if len(robots) == 0:
        print("No tienes robots para vender")
        menu()
    print("¿Que robot quieres vender?")
    for i in range(len(robots)):
        print(f"{i+1}. {robots[i].get_name()} - ${25}")
    print(f"{len(robots)+1}. Volver al menu")
    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == str(len(robots)+1):
        menu()
    elif opcion.isdigit() and int(opcion) > 0 and int(opcion) <= len(robots):
        money += 25
        del robots[int(opcion)-1]
        print("Robot vendido!")
    else:
        print("Opcion no valida")
        vender_robot()
    menu()

def ver_robots():
    if len(robots) == 0:
        print("No tienes robots")
        menu()
    print("tus robots:")
    for i in range(len(robots)):
        print(f"{i+1}. {robots[i].get_name()} - Batery: {robots[i].get_batery()} - Shield: {robots[i].get_shield()}")
    print(f"{len(robots)+1}. Volver al menu")
    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == str(len(robots)+1):
        menu()
    else:
        print("Opcion no valida")
        ver_robots()
    menu()

def luchar():
    global money
    if len(robots) == 0:
        print("No tienes robots para luchar")
        menu()
    print("elige tu robot para luchar:")
    for i in range(len(robots)):
        print(f"{i+1}. {robots[i].get_name()} - Batery: {robots[i].get_batery()} - Shield: {robots[i].get_shield()}")
    print(f"{len(robots)+1}. Volver al menu")
    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == str(len(robots)+1):
        menu()
    elif opcion.isdigit() and int(opcion) > 0 and int(opcion) <= len(robots):
        robot_jugador = robots[int(opcion)-1]
        robot_enemigo = random.choice(robots)
        while robot_jugador.get_batery() > 0 and robot_enemigo.get_batery() > 0:
            ataque_jugador = random.randint(10, 30)
            ataque_enemigo = random.randint(10, 30)
            robot_enemigo.set_batery(robot_enemigo.get_batery() - ataque_jugador)
            robot_jugador.set_batery(robot_jugador.get_batery() - ataque_enemigo)
            print(f"Tu robot ataca con {ataque_jugador} de daño!")
            print(f"El robot enemigo ataca con {ataque_enemigo} de daño!")
        if robot_jugador.get_batery() > 0:
            print("¡Ganaste la batalla!")
            print("Recibiste $25 por ganar la batalla!")
            money += 25
        else:
            print("Perdiste la batalla...")
    else:
        print("Opcion no valida")
        luchar()
    input("(presione Enter para volver al menú)")
    menu()

menu()
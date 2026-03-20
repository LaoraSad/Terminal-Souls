import random
from funciones import generar_daño, atacar, curar, habilidad_especial

print("-----Welcome to Terminal Souls-----\n")

print("-----Initial Attributes-----\n"
    "Hp Hero: 100\n" 
    "healing potions: 3\n"
    "Hp Enemy: 120\n")

hp_heroe = 100
potion = 3
hp_enemy = 120

while hp_heroe > 0 and hp_enemy > 0:
    print("-----Menu-----\n"
          "1. Atacar\n"
          "2. Curar\n"
          "3. Habilidad especial\n")
    
    elegir = int(input("elija la opcion que deseas: ")) 


    if elegir == 1:
        hp_enemy = atacar(hp_enemy)

    elif elegir == 2:
        if potion == 0:
            print("no tienes pociones disponibles, elige nuevamente")
            continue  
        hp_heroe, potion = curar(hp_heroe, potion)
        

    elif elegir == 3:
        hp_enemy = habilidad_especial(hp_enemy)
    
    if hp_enemy > 0:
        daño_enemigo = generar_daño(15,20)
        hp_heroe -= daño_enemigo

    if hp_heroe < 0:
        hp_heroe = 0

    print(f"El enemigo te hizo {daño_enemigo} de daño")
    print(f"Hp actual: {hp_heroe}")

if hp_heroe <= 0:
    print("💀 Has perdido")
else:
    print("🏆 Has ganado")

    



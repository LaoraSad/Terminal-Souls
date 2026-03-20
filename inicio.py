import random
from funciones import generar_daño, atacar, curar, habilidad_especial, generic_input, sistema_critico
import random
print(" 🕹️ 🕹️ 🕹️ 🕹️ Welcome to Terminal Souls 🕹️ 🕹️ 🕹️ 🕹️\n")

print(" ⭐ ⭐ ⭐ Initial Attributes ⭐ ⭐ ⭐ \n"
    "⚜️  Hp Hero: 100\n" 
    "🫙  healing potions: 3\n"
    "⚜️  Hp Enemy: 120\n")

hp_heroe = 100
potion = 3
hp_enemy = 120

while hp_heroe > 0 and hp_enemy > 0:
    print("-----Menu-----\n"
          "1. ⚔️ Atacar\n"
          "2. 🛠️ Curar\n"
          "3. ✨ Habilidad especial\n")
    
    elegir = generic_input("elija la opcion que deseas: ", False,int) 
    if elegir in [1,2,3]:
            opcion_valida = True
    else:
        print("solo puedes escoger 1, 2 o 3, intenta nuevamente\n")
        continue
        

    if elegir == 1:
        print("ha atacado el enemigo:")
        hp_enemy = atacar(hp_enemy)
        print("=" * 40)
        print("el heroe ha sido atacado")
        hp_heroe = atacar(hp_heroe)
        
        

    elif elegir == 2:
        if potion == 0:
            print("cuidado! no tienes pociones disponibles, elige nuevamente")
            continue  
        hp_heroe, potion = curar(hp_heroe, potion)
        hp_heroe = atacar(hp_heroe)
        

    elif elegir == 3:
        hp_enemy = habilidad_especial(hp_enemy)
    

    daño_enemigo = generar_daño(15,20)
        # hp_heroe -= daño_enemigo


        # hp_heroe = 0
        # hp_heroe = atacar(hp_heroe)

    print(f"El enemigo te hizo {daño_enemigo} de daño")
    print(f"Hp actual: {hp_heroe}")

if hp_heroe <= 0:
    print("💀 Has perdido")
else:
    print("🏆 Has ganado")

    



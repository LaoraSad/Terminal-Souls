from funciones import  turno_jugador, turno_enemigo, curar, habilidad_especial, generic_input, interfaz

print(" 🕹️ 🕹️ 🕹️ 🕹️ Welcome to Terminal Souls 🕹️ 🕹️ 🕹️ 🕹️\n")

print(" ⭐ ⭐ ⭐ Initial Attributes ⭐ ⭐ ⭐ \n"
    "⚜️  Hp Hero: 100\n" 
    "🫙  healing potions: 3\n"
    "⚜️  Hp Enemy: 120\n")

hp_heroe = 100
potion = 3
hp_enemy = 120

while hp_heroe > 0 and hp_enemy > 0:

    interfaz(hp_heroe, hp_enemy, potion)

    print("-----Menu-----\n"
          "1. ⚔️  Atacar\n"
          "2. 🛠️  Curar\n"
          "3. ✨ Habilidad especial\n")
    
    elegir = generic_input("elija la opcion que deseas: ", False,int) 
    if elegir in [1,2,3]:
            opcion_valida = True
    else:
        print("solo puedes escoger 1, 2 o 3, intenta nuevamente\n")
        continue
        
    if elegir == 1:
        print("El turno del jugador:")
        hp_enemy = turno_jugador(hp_enemy)
        
    elif elegir == 2:
        if potion == 0:
            print("cuidado! no tienes pociones disponibles, elige nuevamente")
            continue  
        hp_heroe, potion = curar(hp_heroe, potion)
         
    elif elegir == 3:
        hp_enemy = habilidad_especial(hp_enemy)
        
    print("=" * 40)
    print("Turno del enemigo")
    hp_heroe, hp_enemy = turno_enemigo(hp_heroe, hp_enemy)


if hp_heroe <= 0: 
    print("💀 Has perdido")
else:
    print("🏆 Has ganado")

    



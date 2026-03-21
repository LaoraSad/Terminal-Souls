from funciones import  turno_jugador, turno_enemigo, curar, habilidad_especial, generic_input, interfaz
import time

print("\n🕹️🕹️🕹️🕹️  WELCOME TO TERMINAL SOULS  🕹️🕹️🕹️🕹️\n")

print("⭐ ⭐ ⭐ INITIAL STATS ⭐ ⭐ ⭐\n"
      "⚜️  Hero HP: 100\n"
      "⚜️  Healing Potions: 3\n"
      "⚜️  Enemy HP: 120")

hp_heroe = 100
potion = 3
hp_enemy = 120

while hp_heroe > 0 and hp_enemy > 0:

    interfaz(hp_heroe, hp_enemy, potion)

    print("\n" + "-" * 40)

    print("\n----- MENU -----\n"
      "1. ⚔️  Attack\n"
      "2. 🧪  Heal\n"
      "3. ✨ Special Ability\n")
    
    print("\n" + "-" * 40)
    
    elegir = generic_input("\n🎮 What will you do? (1-3): ", False, int)
    if elegir in [1,2,3]:
            opcion_valida = True
    else:
        print("❌ Invalid choice! Please select 1, 2, or 3.\n")
        continue

    print("\n" + "-" * 40)   

    if elegir == 1:
        print("🦸‍♀️ Your turn:")
        hp_enemy = turno_jugador(hp_enemy)
        
    elif elegir == 2:
        if potion == 0:
            print("🧪 You reach for a potion...")
            time.sleep(2)
            print("❌ But your inventory is empty!")
            continue  
        hp_heroe, potion = curar(hp_heroe, potion)
         
    elif elegir == 3:
        hp_enemy = habilidad_especial(hp_enemy)
        
    print("=" * 40)
    print("👹 Enemy's turn...")
    hp_heroe, hp_enemy = turno_enemigo(hp_heroe, hp_enemy)

if hp_heroe <= 0:
    print("💀 You have been defeated...")
else:
    print("🏆 Victory! You defeated the enemy!")

    



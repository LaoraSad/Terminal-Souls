from funciones import  player_turn, enemy_turn, cure, special_ability, generic_input, interface
import time

print("\n🕹️🕹️🕹️🕹️  WELCOME TO TERMINAL SOULS  🕹️🕹️🕹️🕹️\n")

print("⭐ ⭐ ⭐ INITIAL STATS ⭐ ⭐ ⭐\n"
      "⚜️  Hero HP: 100\n"
      "⚜️  Healing Potions: 3\n"
      "⚜️  Enemy HP: 120")
time.sleep(1)

hp_heroe = 100
potion = 3
hp_enemy = 120

while hp_heroe > 0 and hp_enemy > 0:

    interface(hp_heroe, hp_enemy, potion)

    print("\n" + "-" * 40)

    print("\n----- MENU -----\n"
      "1. ⚔️  Attack\n"
      "2. 🧪  Heal\n"
      "3. ✨ Special Ability\n")
    
    print("\n" + "-" * 40)
    
    select = generic_input("\n🎮 What will you do? (1-3): ", False, int)
    if select in [1,2,3]:
            valid_option = True
    else:
        print("❌ Invalid choice! Please select 1, 2, or 3.\n")
        continue

    print("\n" + "-" * 40)   

    if select == 1:
        print("🦸‍♀️ Your turn:")
        time.sleep(1)
        hp_enemy = player_turn(hp_enemy)
        
    elif select == 2:
        if potion == 0:
            print("🧪 You reach for a potion...")
            time.sleep(2)
            print("❌ But your inventory is empty!")
            continue  
        hp_heroe, potion = cure(hp_heroe, potion)
         
    elif select == 3:
        hp_enemy = special_ability(hp_enemy)

    
    if hp_enemy > 0:   
        print("=" * 40)
        print("👹 Enemy's turn...")
        hp_heroe, hp_enemy = enemy_turn(hp_heroe, hp_enemy)
        time.sleep(3)
    
        

if hp_heroe <= 0:
    time.sleep(1)
    print("\n💀 You have been defeated...")
else:
    time.sleep(1)
    print("\n🏆 Victory! You defeated the enemy!")

    



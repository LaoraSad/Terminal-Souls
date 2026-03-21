import random


def bar(value, maximum):
    """
    Generates a visual progress bar for HP.

    Args:
        value (int): Current value.
        maximum (int): Maximum value.

    Returns:
        str: A string representing the progress bar.
    """
    if value < 0:
        value = 0

    size = 10
    filled = int((value / maximum) * size)
    empty = size - filled

    return "█" * filled + "░" * empty

def interface(hp_heroe:int, hp_enemy:int, potion:int, hp_max_heroe:int=100, hp_max_enemy:int=120) -> None:
    """
    Displays the game interface showing the hero and enemy status.

    Args:
        hp_heroe (int): Current health points of the hero.
        hp_enemy (int): Current health points of the enemy.
        potion (int): Number of potions available.
        hp_max_heroe (int, optional): Maximum HP of the hero. Defaults to 100.
        hp_max_enemy (int, optional): Maximum HP of the enemy. Defaults to 120.

    Returns:
        None
    """
    emoji =  "🧪" if potion > 0 else "⚠️"
    print("\n" + "=" * 40)  

    print("🦸‍♀️ HEROE")
    print(f"POTIONS {emoji}: {potion}")
    print(f"HP: [{bar(hp_heroe, hp_max_heroe)}] {hp_heroe} / {hp_max_heroe}")

    print()
    
    print("👹 ENEMY")
    print(f"HP: [{bar(hp_enemy, hp_max_enemy)}] {hp_enemy} / {hp_max_enemy}")

def generate_damage(min_daño: int, max_daño: int) -> int:

    """
    returns a random integer between the specified
    minimum and maximum damage values.

    Args:
        min_daño (int): Minimum damage value.
        max_daño (int): Maximum damage value.

    Returns:
        int: Randomly generated damage value.
    """
    return random.randint(min_daño, max_daño)

def player_turn(hp_enemy: int) -> int:
    """
    A random damage value is generated (with a chance of critical hit),
    and the enemy's HP is reduced accordingly.

    Args:
        hp_enemy (int): Current health points of the enemy.

    Returns:
        int: Updated enemy HP after taking damage.
    """

    damage = critical_system()
    hp_enemy -= damage

    if hp_enemy < 0:
        hp_enemy = 0

    print(f"⚔️  You strike the enemy for {damage} damage!")
    print(f"Enemy HP: {hp_enemy}")

    return hp_enemy 

def enemy_turn(hp_heroe:int, hp_enemy:int) -> tuple[int,int]:
    """
     The enemy can either:
    - Attack the hero and deal damage
    - Heal itself if its HP is low (with a probability)

    Args:
        hp_heroe (int): Current health points of the hero.
        hp_enemy (int): Current health points of the enemy.

    Returns:
        tuple[int, int]: Updated (hero HP, enemy HP).
    """

    damage = generate_damage(15,20)
    if hp_enemy <= 24:
        heal_enemy = random.randint(1,10)
        if heal_enemy <= 5:
            hp_enemy += random.randint(20,25)
            print(f"👹 Enemy healed! New HP: {hp_enemy}")

            return hp_heroe, hp_enemy
        
    hp_heroe -= damage 

    if hp_heroe < 0:
        hp_heroe = 0

    print(f"💥 You received {damage} damage!")
    return hp_heroe, hp_enemy

def cure(hp_heroe: int, potion:int)-> tuple[int,int]:
    """
      If potions are available, the hero recovers HP and
    the potion count decreases. If not, no action is taken.

    Args:
        hp_heroe (int): Current health points of the hero.
        potion (int): Number of potions available.

    Returns:
        tuple[int, int]: Updated (hero HP, remaining potions)
    """

    if potion == 0:
        print("❌ You have no potions left! Choose another action.")
        return hp_heroe, potion
    
    hp_heroe += 20 
    if hp_heroe >100:
        hp_heroe = 100
    potion -= 1

    print(f"\n🧪 You used a potion and recovered 20 HP!\n"
        f"HP: {hp_heroe} | Potions left: {potion}")
    
    return hp_heroe, potion 

def special_ability(hp_enemy:int) -> int:
    """
    There is a 50% chance to fail. If successful, it deals
    high random damage to the enemy.

    Args:
        hp_enemy (int): Current health points of the enemy.

    Returns:
        int: Updated enemy HP after the ability
    """

    fail = random.random() < 0.5
    if fail:
        print("❌ Special ability failed!")
        return hp_enemy
    
    damage = generate_damage(30,50)
    hp_enemy -= damage
    if hp_enemy < 0: 
        hp_enemy = 0

    print(f"✨ Special attack dealt {damage} damage!\n"
      f"Enemy HP: {hp_enemy}")
    return hp_enemy

def generic_input(mensaje: str, menor: bool, normalized: int | float | None = None) -> str | int | float: 
    """
    Handles user input with validation and optional type conversion.

    Args:
        mensaje (str): Message displayed to the user.
        menor (bool): If True, ensures the number is positive.
        normalized (type, optional): Type to convert input into (int, float, or None).

    Returns:
        str | int | float: The validated and optionally converted user input.
    """

    valid = False

    while not valid:
        try:
            user_input = input(mensaje).strip().lower()
            
            if user_input is None:
                print("⚠️ Please enter a valid value.")

            if menor:
                if user_input <=0:
                    print("⚠️ Please enter a valid value.")
            
            
            if normalized is None:
                return user_input
            
            if normalized in [int, float]:
                return normalized(user_input)
            
            return normalized(user_input)

        except ValueError: 
            print("⚠️ Please enter a valid value.")

def critical_system()-> int:
    """
    Calculates attack damage with a chance of critical hit.

    There is a 10% chance to deal double damage.

    Returns:
        int: Final damage value.
    """

    critico = random.random() < 0.10
    damage = generate_damage(10,25)

    if critico:
        print("🔥 CRITICAL HIT! Double damage!")
    
        return damage * 2

    return damage


import random
def generar_daño(min_daño: int, max_daño: int) -> int:

    """
    Genera un valor de daño aleatorio dentro de un rango.

    Args:
        min_daño (int): Daño mínimo.
        max_daño (int): Daño máximo.

    Returns:
        int: El daño generado.
    """
    return random.randint(min_daño, max_daño)

     
def atacar(hp_enemy: int) -> int:
    """
    Genera el ataque al enemigo dentro del valor de daño aleatorio dentro de un rango.

    Args:
        hp_enemy (int): Vida del enemigo.

    Returns:
        int: nueva Hp del enemigo.
    """

    daño = generar_daño(10, 25)
    hp_enemy -= daño

    if hp_enemy < 0:
        hp_enemy = 0

    print(f"hiciste {daño} de daño")
    print(f"hp enemigo: {hp_enemy}")

    return hp_enemy 

def curar(hp_heroe: int, potion:int)-> tuple:
    if potion == 0:
        print("no tienes pociones disponibles, elige nuevamente")
        return hp_heroe, potion
    
    hp_heroe += 20 
    if hp_heroe >100:
        hp_heroe = 100
    potion -= 1

    print(f"acabas de usar una pocion, recuperaste 20 de Hp\n"
            f"Hp: {hp_heroe}, pociones disponibles: {potion}")
    
    return hp_heroe, potion 

def habilidad_especial(hp_enemy:int) -> int:
    fallar = random.random() < 0.5
    if fallar:
        print("fallaste la habilidad especial")
        return hp_enemy
    
    daño = generar_daño(30,50)
    hp_enemy -= daño
    if hp_enemy < 0: 
        hp_enemy = 0

    print(f"se realizo {daño} de daño\n"
        f"Hp del enemigo: {hp_enemy}")
    return hp_enemy

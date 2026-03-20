# Terminal Souls 🕹️

## 📌 Description

Terminal Souls is a turn-based combat game developed in Python.
The player controls a hero who fights against an enemy using different actions such as attacking, healing, and using a special ability.

---

## ⚙️ Features

* Turn-based combat system
* Random damage generation using the `random` module
* Healing system with limited potions
* Special ability with a probability of failure
* Automatic enemy attacks after each valid turn

---

## 🧠 Game Mechanics

* The hero starts with **100 HP** and **3 healing potions**
* The enemy starts with **120 HP**
* Each turn, the player chooses an action:

  * **Attack** → deals random damage between 10 and 25
  * **Heal** → restores 20 HP (if potions are available)
  * **Special Ability** → deals 30–50 damage but has a 50% chance to fail
* If the player tries to heal without potions, the turn is skipped
* After each valid action, the enemy attacks automatically
* The game ends when either the hero or the enemy reaches **0 HP**

---

## 🧩 Project Structure

```
main.py        # Game loop and player interaction
funciones.py   # Game logic (functions)
```

---

## 🧪 Functions

* `generar_daño(min_dano, max_dano)`
  Generates a random damage value within a range

* `atacar(hp_enemy)`
  Applies damage to the enemy and ensures HP does not go below 0

* `curar(hp_heroe, potion)`
  Restores 20 HP and decreases the number of potions

* `habilidad_especial(hp_enemy)`
  Performs a powerful attack with a chance to fail

---

## ▶️ How to Run

1. Make sure Python is installed
2. Place the files in the same folder:

   * `main.py`
   * `funciones.py`
3. Run the program:

```bash
python main.py
```

---

## 📚 Concepts Used

* Functions
* Conditionals (`if`, `elif`, `else`)
* Loops (`while`)
* Random module
* Modular programming

---

## 👤 Author






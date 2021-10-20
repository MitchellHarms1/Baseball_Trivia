import time
#import numpy as np --- Error "ModuleNotFoundError: No module named 'numpy'"
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==========='):
        # Save variables as attributes 
        self.name = name
        self.type = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health 
        self.bars = 20 # Amount of health bars

def fight(self, Pokemon2):
    # Allows two pokemon to fight

    # Print fight information
    print("-----POKEMON BATTLE-----")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK", self.attack)
    print("DEFENSE", self.defense)
    #print("LVL/", 3*(1+np.mean([self.attack,self.defense]))) ---- numpy error
    print("\nVS")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK", Pokemon2.attack)
    print("DEFENSE", Pokemon2.defense)
    #print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense]))) ---- numpy error

    time.sleep(2)

    # Consider type advantages 
    version = ['Fire', 'Water', 'Grass']
    for i,k in enumerate(version):
        if self.types == k:
            # Both pokemon are the same type
            string_1_attack = "Its not very effective..."
            string_2_attack = "Its not very effective..."

            # Pokemon2 is super effective
            if Pokemon2.types == version[(i+1)%3]:
                Pokemon2.attack *= 1.5
                Pokemon2.defense *= 1.5
                self.attack /= 1.5
                self.defense /= 1.5
                string_1_attack = "Its not very effective..."
                string_2_attack = "Its super effective!"

            # Pokemon2 is not very effective
            if Pokemon2.types == version[(i+2)%3]:
                self.attack *= 1.5
                self.defense *= 1.5
                Pokemon2.attack /= 1.5
                Pokemon2.defense /= 1.5
                string_1_attack = "Its not very effective..."
                string_2_attack = "Its super effective!"

# Now for the actual fighting
# Continue while pokemon still have health
    while (self.bars > 0) and (Pokemon2.bars > 0):
        # Print the health of each pokemon
        print(f"{self.name}\t\HLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\HLTH\t{Pokemon2.health}")

        print(f"Go {self.name}!")
        for i, x in enumerate(self.moves):
            print(f"{i+1}.", x)
        
        index = int(input('Pick a move: '))
        delay_print(1)
        time.sleep(1)
        delay_print(string_1_attack)

        # Determine damage
        Pokemon2.bars -= self.attack
        Pokemon2.health = ""

        # Add back bars plus defensive boost
        for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
            Pokemon2.health += "="
        
        time.sleep(1)
        print(f"{self.name}\t\HLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\HLTH\t{Pokemon2.health}")
        time.sleep(.5)

        # Check to see if pokemon fainted
        if Pokemon2.bars <= 0:
            delay_print("\n..." + Pokemon2.name + ' fainted.')
            break

        # Pokemon2's turn to attack
        print(f"Go {Pokemon2.name}!")
        for i, x in enumerate(Pokemon2.moves):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        delay_print(f"{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
        time.sleep(1)
        delay_print(string_2_attack)

        # Determine damage
        self.bars -= Pokemon2.attack
        self.health = ""

        # Add back bars plus defensive boost
        for j in range(int(self.bars+.1*self.defense)):
            self.health += "="
        
        time.sleep(1)
        print(f"{self.name}\t\HLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\HLTH\t{Pokemon2.health}")
        time.sleep(.5)

        # Check to see if pokemon fainted
        if self.bars <= 0:
            delay_print("\n..." + self.name + ' fainted.')
            break
#money = np.random.choice(5000)
#delay_print(f"Opponent paid you ${money}.") ---- Numpy error 

if__name__ == '__main__':
    #Create pokemon
    
   Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Dragon Claw'], {'ATTACK': 12, 'DEFENSE': 8})
   Politoed = Pokemon('Politoed', 'Water', ['Weather Ball (Water)', 'Earthquake', 'Blizzard', 'Scald'], {'ATTACK': 9, 'DEFENSE': 11})
   Meganium = Pokemon('Meganium', 'Grass', ['Frenzy Plant', 'Earthquake', 'Vine Wipe', 'Petal Blizzard'], {'ATTACK': 7, 'DEFENSE': 13})

Charizard.fight(Politoed) # Get them to battle 


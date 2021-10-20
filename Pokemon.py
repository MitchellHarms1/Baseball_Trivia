import sys
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

movesetAZ = ["Play Rough", "Liquidation", "Aqua Jet", "Super Power"]
movesetUM = ["Moonlight", "Wish", "Last Resort", "Fient Attack"]

class Pokemon1():
    def __init__(self, attack, defense, hp, types, moves):
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.types = types
        self.moves = moves


azumarill = Pokemon1('50', '80', '100', 'Water / Fairy', movesetAZ)
umbreon = Pokemon1('40', '90', '100', 'Dark', movesetUM)



print(azumarill.moves)
    
#print("Go Azumarill!")
#for i, x in enumerate(azumarill.moves):
 #   print(f"{i+1}.", x)
 #   index = int(input('Pick a move: '))
 #   delay_print("Azumarill used {azumarill.moves[index-1]}!")
  #  time.sleep(1)

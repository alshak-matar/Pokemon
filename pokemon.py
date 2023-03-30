import time
import numpy as np
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20
    

    def fight(self, Pokemon2):
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE:/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE:/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = '\n Ce n est pas très efficace...'
                    string_2_attack = '\n Ce n est pas très efficace...'

                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\n Ce n est pas très efficace'
                    string_2_attack = '\n C est super efficace!'
                
                if Pokemon2.types == version[(i+1)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.attack /= 2
                    string_1_attack = '\n C est super efficace'
                    string_2_attack = '\n Ce n est pas très efficace...'
            while (self.bars) and (Pokemon2.bars > 0):
                print(f"{self.name}\t\tHLTH\t{self.health}")
                print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

                print(f"Go {self.name}!")
                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                index = int(input('Choisissez un mouvement: '))
                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)

                Pokemon2.bars -= self.attack
                Pokemon2.health = ""


                for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                    Pokemon2.health += "="

                time.sleep(1)

                print(f"\n{self.name}\t\tHLTH\t{self.health}")
                print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
                time.sleep(.5)

                if Pokemon2.bars <= 0:
                    delay_print("\n..." + Pokemon2.name + 'fainted.')
                    break


                print(f"Go {Pokemon2.name}!")
                for i, x in enumerate(Pokemon2.moves):
                    print(f"{i+1}.", x)
                index = int(input('Pick a move: '))
                delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_2_attack)

                self.bars -= Pokemon2.attack
                self.health = ""


                for j in range(int(self.bars+.1*self.defense)):
                    self.health += "="

                time.sleep(1)

                print(f"\n {self.name}\t\tHLTH\t{self.health}")
                print(f"\n {Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
                time.sleep(0.5)

                if self.bars <= 0:
                    delay_print("\n..." + self.name + 'fainted.')
                    break
            money = np.random.choice(5000)
            delay_print(f"\n L'adversaire vous a payé €{money}.")




if __name__ == '__main__':
    Dracaufeu = Pokemon('Dracaufeu', 'Feu', ['Lance-flammes', 'voler', ' Brûlure', 'Coup de feu'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Eau', ['Pistolet à eau', 'Faisceau de bulle', 'Pompe hydraulique', 'Le surf'], {'ATTACK':10, 'DEFENSE': 10})
    Florizarre = Pokemon('Florizarre', 'Herbe', ['Lingette de vigne', 'Feuille de rasoir', 'Tremblement de terre', 'Plante frénétique'], {'ATTACK':8, 'DEFENSE': 12})

    Salamèche = Pokemon('Salamèche', 'Feu', ['braise', 'Gratter', 'Attaquer', 'Coup de feu'], {'ATTACK':4, 'DEFENSE': 2})
    Carapuce = Pokemon('Carapuce', 'Eau', ['Faisceau de bulle', 'Attaquer', 'Coup de tête', 'Le surf',], {'ATTACK':3, 'DEFENSE': 3})
    Bulbizarre = Pokemon('Bulbizarre', 'Herbe', ['Lingette de vigne', 'Feuille de rasoir', 'Attaquer', 'Graine de sangsue',], {'ATTACK':2, 'DEFENSE': 4})

    Charméléon = Pokemon('Charméléon', 'feu', ['braise', 'Gratter', 'Lance-flammes', 'Coup de feu',], {'ATTACK':6, 'DEFENSE': 5})
    Tortue = Pokemon('Tortue', 'Eau', ['Faisceau de bulle', 'Pistolet à eau', 'Pistolet à eau', 'Le Surf',], {'ATTACK':5, 'DEFENSE': 5})
    Ivysaure = Pokemon('Ivysaure\t', 'Herbe', ['Lingette de vigne', 'Feuille de rasoir', 'Graine de balle', 'Graine de sangsue',], {'ATTACK':4, 'DEFENSE': 6})

    Dracaufeu.fight(Blastoise)

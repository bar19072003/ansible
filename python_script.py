#!/usr/bin/env python3

class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self):
        print(self.name + " attack the enemies!")

    def life_check(self):
        print(f"your player has {self.life} life remaining.")


player1 = GameCharacter("bar", 100)
player2 = GameCharacter("oren", 100)

player1.attack()
player2.life_check()

class bar(GameCharacter):
    def p(self):
        print("hello world")

player3 = bar("bib", 1000)

player3.life_check()
player3.p()

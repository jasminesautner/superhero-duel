import random

class Ability:
    # attack_strength is the max attack a user could possibly have

    def __init__(self, name, attack_strength):
        # initialize starting values
        self.name = name
        self.attack_strength = attack_strength
    
    def attack(self):
        # calculate lowest attack value as an integer
        attack_strength = self.attack_strength
        min_attack = attack_strength // 2
        # use random.randint(a, b) to select random attack value
        attack = random.randint(min_attack, attack_strength)
        # return attack value between 0 and full attack
        return attack

    def update_attack(self, attack_strength):
        # update attack value
        # self.attack_strength.append(attack_strength)
        return attack_strength
        
class Hero(Ability):

    def __init__(self, name):
        # initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # append abbility to self.abilities
        self.abilities.append(ability)

    def attack(self):
        total = 0
        # run attack() on every ability hero has
        for ability in self.abilities:
           total += ability.attack()
        return total

class Weapon(Ability):
    def attack(self):
        max_attack = self.attack_strength
        weapon_attack = random.randint(0, max_attack)
        return weapon_attack

class Team: 
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 
        return 0 

    def find_hero(self, name):
 
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        print(self.heroes)


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())





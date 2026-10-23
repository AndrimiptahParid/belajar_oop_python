class Hero: # templat
    
    def __init__(self, inputName, inputPower, inputHealth, inputpower):
        self.name = inputName
        self.power = inputPower
        self.health = inputHealth
        self.power = inputpower

hero1 = Hero("Superman", 100, 100, 50)
hero2 = Hero("Batman", 80, 120, 60)

print(f"hero1: {hero1.name}, power: {hero1.power}, health: {hero1.health}")
print(f"hero2: {hero2.name}, power: {hero2.power}, health: {hero2.health}")
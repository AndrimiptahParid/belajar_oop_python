class Hero:
    #class variabel
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
     # void function, method tanpa return
    def siapa(self):
        print(f"namaku adalah {self.name}")
        
     # method dengan argumen   
    def healthUp(self, up):
        self.health += up
        
    # method dengan return
    def getHealth(self):
        return self.health
    
hero1 = Hero("Superman", 100, 50, 20)
hero2 = Hero("batman", 1000, 500, 200)

hero1.siapa()
hero1.healthUp(20)
print(hero1.getHealth())

hero2.siapa()
hero2.healthUp(100)
print(hero2.getHealth())
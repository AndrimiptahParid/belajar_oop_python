class hero:
    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor
    
    def attack(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)
        
    def diserang(self, lawan, attackPower):
        print(self.name + ' diserang ' + lawan.name)
        damage = attackPower / self.armor
        print('serangan menyebabkan ' + str(damage) + ' damage')
        self.health -= damage
        print('darah ' + self.name + ' tersisa ' + str(self.health))
        
sniper = hero("sniper", 100, 30, 40)
ahmad = hero("ahmad", 100, 20, 50)

sniper.attack(ahmad)
ahmad.attack(sniper)

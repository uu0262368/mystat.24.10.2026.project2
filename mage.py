class Mage:
    def __init__(self, name, health, attack_power, critical_chance, mana):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.critical_chance = critical_chance
        self.mana = mana

    def attack(self, target):
        target.health = target.health - self.attack_power
        print(f"{self.name} атакует {target.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def special(self, warrior, rogue):
        if self.mana >= 20:
            warrior.attack_power = warrior.attack_power *2
            rogue.attack_power = rogue.attack_power *2
            print(f"{self.name} использует заклинание, увеличивая силу союзников в 2 раза!")
        else:
            print(f"{self.name} не хватает маны для использования заклинания!")
        self.mana -= 20
    critical_chance=0

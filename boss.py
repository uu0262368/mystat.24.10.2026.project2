class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        if self.is_alive():
            target.take_damage(self.attack_power)
            print(f"{self.name} атакует {target.name} на {self.attack_power} урона!")

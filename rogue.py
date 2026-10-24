class Rogue:
    def __init__(self, name, health, attack_power, critical_chance):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.critical_chance = critical_chance

    def attack(self, target):
        target.health = target.health - self.attack_power
        print(f"{self.name} атакует {target.name} на {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def special(self, target):
        target.health = target.health - (self.attack_power * 3)
        print(f"{self.name} подкрадывается к {target.name} и наносит ему скрытый удар!")

    critical_chance=0

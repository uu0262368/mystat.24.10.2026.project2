import mage
import rogue
import warrior
import boss
from random import randint

mage_player = mage.Mage("Маг", 0, 0, 0, 0)
rogue_player = rogue.Rogue("Ассасин", 0, 0, 0)
warrior_player = warrior.Warrior("Воин", 0, 0, 0)
enemy_unit = boss.Enemy("Враг", 0, 0)


def stats(character):
    print(f"Указать характеристики вам собственно ручно, или рандомно для персонажа {character.name}? (1 - ручной ввод, 2 - рандом)")
    choice = int(input())
    if choice == 1:
        if character == mage_player:
            char = "Маг"
        elif character == rogue_player:
            char = "Ассасин"
        elif character == warrior_player:
            char = "Воин"
        else:
            char = "Враг"

        print(f"Какое имя вы хотите дать персонажу {char}?")
        character.name = input()
        print(f"Введите количество здоровья персонажа {char}:")
        character.health = int(input())
        print(f"Введите силу атаки персонажа {char}:")
        character.attack_power = int(input())
        if char != "Враг":
            print(f"Введите шанс специальной атаки персонажа {char}:")
            character.critical_chance = int(input())

        if char == "Маг":
            print(f"Введите количество маны персонажа {char}:")
            character.mana = int(input())
    if choice == 2:
        if character == mage_player:
            char = "Маг"
        elif character == rogue_player:
            char = "Ассасин"
        elif character == warrior_player:
            char = "Воин"
        else:
            char = "Враг"
        print(f"Вы выбрали рандомные характеристики для персонажа {char}.")

        character.name = f"{char}"
        character.health = randint(50, 150)
        character.attack_power = randint(5, 20)
        if char != "Враг":
            character.critical_chance = randint(1, 100)

        if char == "Маг":
            character.mana = randint(10, 50)

def main():
    while enemy_unit.is_alive():
        if mage_player.is_alive():
            mage_player.attack(enemy_unit)
            if enemy_unit.is_alive():
                enemy_unit.attack(mage_player)
            crit = randint(1, 100)
            if crit <= mage_player.critical_chance:
                mage_player.special(warrior_player, rogue_player)
                mage_player.critical_chance = 0
        if rogue_player.is_alive():
            rogue_player.attack(enemy_unit)
            if enemy_unit.is_alive():
                enemy_unit.attack(rogue_player)
            crit = randint(1, 100)
            if crit <= rogue_player.critical_chance:
                rogue_player.special(enemy_unit)
        if warrior_player.is_alive():
            warrior_player.attack(enemy_unit)
            if enemy_unit.is_alive():
                enemy_unit.attack(warrior_player)
            crit = randint(1, 100)
            if crit <= warrior_player.critical_chance:
                warrior_player.special(enemy_unit)
        if not mage_player.is_alive() and not rogue_player.is_alive() and not warrior_player.is_alive() and enemy_unit.is_alive():
            print("Все игроки мертвы! Враг победил!")
            break
        elif not enemy_unit.is_alive():
            print("Враг мертв! Игроки победили!")
            break
        elif not mage_player.is_alive() and not rogue_player.is_alive() and not warrior_player.is_alive() and not enemy_unit.is_alive():
            print("Все мертвы! Ничья!")
            break

stats(mage_player)
stats(rogue_player)
stats(warrior_player)
stats(enemy_unit)
print(f"Начинаем бой! Игроки: {mage_player.name}, {rogue_player.name}, {warrior_player.name} против врага: {enemy_unit.name}")
print(f"Хотите просмотреть характеристики игроков и врага перед боем? (1 - да, 2 - нет)")
choice_stats = int(input())
if choice_stats == 1:
    print(f"Характеристики {mage_player.name}: Здоровье - {mage_player.health}, Сила атаки - {mage_player.attack_power}, Шанс специальной атаки - {mage_player.critical_chance}, Мана - {mage_player.mana}")
    print(f"Характеристики {rogue_player.name}: Здоровье - {rogue_player.health}, Сила атаки - {rogue_player.attack_power}, Шанс специальной атаки - {rogue_player.critical_chance}")
    print(f"Характеристики {warrior_player.name}: Здоровье - {warrior_player.health}, Сила атаки - {warrior_player.attack_power}, Шанс специальной атаки - {warrior_player.critical_chance}")
    print(f"Характеристики врага {enemy_unit.name}: Здоровье - {enemy_unit.health}, Сила атаки - {enemy_unit.attack_power}")
    main()
if choice_stats == 2:
    print("Начинаем бой без просмотра характеристик!")
    main()

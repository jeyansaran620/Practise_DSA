import random

from classes.game import Person, bcolors
from classes.magic import Spell
from  classes.inventory import Item


# black magic
fire=Spell("Fire", 10, 500, "black")
thunder=Spell("Thunder", 12, 580, "black")
blizzard=Spell("Blizzard", 14, 640, "black")
meteor=Spell("Meteor", 16, 720, "black")
blake=Spell("Blake", 18, 800, "black")

# white magic
cure = Spell("Cure", 12, 620, "white")
cura = Spell("Cura", 16, 1500, "white")

player_magic = [fire,thunder,blizzard,meteor,blake,cure,cura]


potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixer", "Fullly restores HP on one member", 99999)
hielixir = Item("MegaElixir", "elixer", "Fullly restores HP for all", 99999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player1_items =[{"item": potion, "quantity": 5},{"item": hipotion, "quantity": 3},
               {"item": superpotion, "quantity": 1},{"item": elixir, "quantity": 3},
               {"item": hielixir, "quantity": 1},{"item": grenade, "quantity": 3}]
player2_items =[{"item": potion, "quantity": 5},{"item": hipotion, "quantity": 3},
               {"item": superpotion, "quantity": 1},{"item": elixir, "quantity": 3},
               {"item": hielixir, "quantity": 1},{"item": grenade, "quantity": 3}]
player3_items =[{"item": potion, "quantity": 5},{"item": hipotion, "quantity": 3},
               {"item": superpotion, "quantity": 1},{"item": elixir, "quantity": 3},
               {"item": hielixir, "quantity": 1},{"item": grenade, "quantity": 3}]

#instantiate people
player1 = Person("Valos",3260, 132, 300, 34, player_magic, player1_items)
player2 = Person("Nick ",4160, 176, 310, 34, player_magic, player2_items)
player3 = Person("Robot",3940, 168, 290, 34, player_magic, player3_items)

enemy1 = Person("Magus",17500, 130, 285, 25, player_magic, [])
enemy2 = Person("Imper",11200, 100, 340, 25, player_magic, [])
enemy3 = Person("Impro",11200, 100, 340, 25, player_magic, [])

players = [player1,player2,player3]
enemies = [enemy1,enemy2,enemy3]

running = True
i=0

while running:
    print("===================================")

    print("\n\n")
    print("NAME                 HP                                     MP")
    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n\n")


    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice)-1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("you attacked", enemies[enemy].name, "for ", dmg )

            if enemies[enemy].get_hp() == 0:
                print(bcolors.OKGREEN + enemies[enemy].name + " had died." + bcolors.ENDC)
                del enemies[enemy]

        elif index==1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice < -1 or magic_choice >= len(player.magic):
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot Enough Magic Points to do this Magic" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                      "points of damage to " + enemies[enemy].name + bcolors.ENDC + "\n")

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name + " had died." + bcolors.ENDC)
                    del enemies[enemy]

            elif spell.type == "white":
                player.heal(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " heals", str(magic_dmg),
                      "points of HP " +  bcolors.ENDC + "\n")


        elif index == 2:

            player.choose_item()

            item_choice = int(input("choose Item: "))-1

            if item_choice < -1 or item_choice >= len(player.items):
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] > 0:

                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop) + bcolors.ENDC)

                elif item.type == "elixer":
                    if item.name == "Elixir":
                        player.hp = player.max_hp
                        player.mp = player.max_mp

                        print(bcolors.OKGREEN + "\n" + item.name + " restored all you" + bcolors.ENDC)

                    elif item.name == "MegaElixir":
                        for target in players:
                            target.hp = target.max_hp
                            target.mp = target.max_mp

                        print(bcolors.OKGREEN + "\n" + item.name + " restored your team." + bcolors.ENDC)

                elif item.type == "attack":

                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item.prop)

                    print(bcolors.OKGREEN + "\n" + item.name + " deals damage of " + str(item.prop) + " to " + enemies[enemy].name + bcolors.ENDC)

                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.OKGREEN + enemies[enemy].name + " had died." + bcolors.ENDC)
                        del enemies[enemy]

                player.reduce_item(item_choice)

            else:
                print(bcolors.FAIL + "you have no " +item.name + bcolors.ENDC)
                continue

   # check for defeats
    defeated_enemies = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    if defeated_enemies > 2:
        print(bcolors.OKGREEN + "you won!" + bcolors.ENDC)
        running = False

    defeated_players = 0
    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_players > 2:
        print(bcolors.FAIL + "you lost!" + bcolors.ENDC)
        running = False


    for enemy in enemies:
        enemy_choice = random.randrange(0,2)

        if enemy_choice == 0:
            target = random.randrange(0,len(players))
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name + " attacked " + players[target].name + " for " + str(enemy_dmg) + bcolors.ENDC)

        elif enemy_choice ==1:

            if enemy.get_mp() > 10:
                spell = enemy.choose_enemy_spell()

                magic_dmg = spell.generate_spell_damage()

                if spell.type == "black":
                    target = random.randrange(0,len(players))
                    players[target].take_damage(magic_dmg)

                    print(bcolors.FAIL + spell.name + " of " + enemy.name + " deals", str(magic_dmg),
                          "points of damage to " + players[target].name + bcolors.ENDC )

                    if players[target].get_hp() == 0:
                        print(bcolors.FAIL + players[target].name + " had died." + bcolors.ENDC)
                        del players[target]

                elif spell.type == "white":
                    enemy.heal(magic_dmg)

                    print(bcolors.WARNING + spell.name + " heals", str(magic_dmg),
                          "points of HP of " + enemy.name + bcolors.ENDC )



            else:
                target = random.randrange(0, len(players))
                enemy_dmg = enemy.generate_damage()
                players[target].take_damage(enemy_dmg)
                print(bcolors.FAIL + enemy.name + " attacked " + players[target].name + " for " + str(
                    enemy_dmg) + bcolors.ENDC)

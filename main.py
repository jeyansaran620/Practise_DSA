from classes.game import Person, bcolors
from classes.magic import Spell
from  classes.inventory import Item

# black magic
fire=Spell("Fire", 10, 100, "black")
thunder=Spell("Thunder", 12, 120, "black")
blizzard=Spell("Blizzard", 14, 140, "black")
meteor=Spell("Meteor", 16, 160, "black")
blake=Spell("Blake", 18, 180, "black")

# white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 16, 180, "white")


potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixer", "Fullly restores HP on one member", 99999)
hielixir = Item("MegaElixir", "elixer", "Fullly restores HP for all", 99999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)



#instantiate people
player = Person(460, 100, 60, 34, [fire,thunder,blizzard,meteor,blake,cure,cura],[potion,hipotion,superpotion,elixir,hielixir,grenade])
enemy = Person(1200, 65, 45, 25, [],[])

running = True
i=0

while running:
    print("===================================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice)-1

    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for ",dmg )

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
            enemy.take_damage(magic_dmg)
        if spell.type == "white":
            player.heal(magic_dmg)

        print(bcolors.OKBLUE + "\n"+ spell.name + " deals", str(magic_dmg) , "points of damage" + bcolors.ENDC)

    elif index==2:
        player.choose_item()
        item_choice= int(input("choose Item: "))-1

        if item_choice < -1 or item_choice >= len(player.items):
            continue
        item = player.items[item_choice]

        if item.type=="potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name +" heals for "+ str(item.prop) +  bcolors.ENDC)

        elif item.type=="elixir":
            player.hp=player.max_hp
            player.mp=player.max_mp
            print(bcolors.OKGREEN + "\n" + item.name +" restored you "+ str(item.prop) +  bcolors.ENDC)

        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " deals damage of " + str(item.prop) + bcolors.ENDC)

    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for ",enemy_dmg)

    print("-------------------------------")
    print("Your Health Points:"+ bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your Magic Points:" + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    print("Enemy Health Points:"+ bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)


    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "you won!"+ bcolors.ENDC)
        running=False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + "you lost!"+ bcolors.ENDC)
        running=False

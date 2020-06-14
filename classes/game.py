import random

class bcolors:
    HEADER = '\033[033m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.name=name
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.actions=["Attack","Magic","Items"]
        self.items=items

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def take_damage(self,dmg):
        self.hp-=dmg
        if self.hp < 0:
            self.hp=0
        return self.hp

    def heal(self,dmg):
        self.hp +=dmg
        if self.hp > self.max_hp:
            self.hp= self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self,cost):
        self.mp -= cost

    def reduce_item(self,choice):
        self.items[choice]["quantity"] -= 1

    def choose_action(self):
        i=1
        print(bcolors.OKBLUE + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    "+ str(i) + ". " + item)
            i+=1

    def choose_magic(self):
        i=1
        print("\n"+ bcolors.OKBLUE+"MAGIC"+bcolors.ENDC)
        for item in self.magic:
            print("    "+ str(i) + ". " + item.name + " " + str(item.cost))
            i+=1

    def choose_item(self):
        i=1
        print("\n"+ bcolors.OKBLUE+"ITEMS"+bcolors.ENDC)
        for item in self.items:
            print("    "+ str(i) + ". " + item["item"].name + ": " + item["item"].description + " - " + bcolors.FAIL + str(item["quantity"]) + bcolors.ENDC)
            i+=1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + "ENEMIES" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.hp > 0:
                print("    " + str(i) + ". " + enemy.name + ": "  + bcolors.ENDC)
            i += 1
        return int(input("select enemy:"))-1

    def get_enemy_stats(self):
        bar_hp = ""
        bar_ticks_hp = (self.hp / self.max_hp) * 50
        for x in range (0, 50):
            if x < int(bar_ticks_hp):
                bar_hp+="█"
            else:
                bar_hp+=" "

        bar_mp = ""
        bar_ticks_mp = (self.mp / self.max_mp) * 10
        for x in range(0, 10):
            if x < int(bar_ticks_mp):
                bar_mp += "█"
            else:
                bar_mp += " "

        hp_range=str(self.max_hp)
        hp_range="/"+hp_range
        hp_range =str(self.hp) + hp_range

        if len(hp_range) < 11:
            for x in range(0, 11 - len(hp_range)):
                hp_range = " " + hp_range

        mp_range = str(self.max_mp)
        mp_range = "/" + mp_range
        mp_range = str(self.mp) + mp_range

        if len(mp_range) < 7:
            for x in range(0, 7 - len(mp_range)):
                mp_range = " " + mp_range

        print("                     __________________________________________________               __________")
        print(bcolors.BOLD + self.name+":  " +
              hp_range + " |" + bcolors.FAIL + bar_hp + bcolors.ENDC + "|     " +

              mp_range + " |" + bcolors.WARNING + bar_mp + bcolors.ENDC + "|")


    def get_stats(self):
        bar_hp = ""
        bar_ticks_hp = (self.hp / self.max_hp) * 25
        for x in range (0, 25):
            if x < int(bar_ticks_hp):
                bar_hp+="█"
            else:
                bar_hp+=" "

        bar_mp = ""
        bar_ticks_mp = (self.mp / self.max_mp) * 10
        for x in range(0, 10):
            if x < int(bar_ticks_mp):
                bar_mp += "█"
            else:
                bar_mp += " "

        hp_range=str(self.max_hp)
        hp_range="/"+hp_range
        hp_range =str(self.hp) + hp_range

        if len(hp_range) < 9:
            for x in range(0, 9 - len(hp_range)):
                hp_range = " " + hp_range

        mp_range = str(self.max_mp)
        mp_range = "/" + mp_range
        mp_range = str(self.mp) + mp_range

        if len(mp_range) < 7:
            for x in range(0, 7 - len(mp_range)):
                mp_range = " " + mp_range

        print("                     _________________________               __________")
        print(bcolors.BOLD + self.name+":    " +
              hp_range + " |" + bcolors.OKGREEN + bar_hp + bcolors.ENDC + "|     " +

              mp_range + " |" + bcolors.OKBLUE + bar_mp + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        spell = self.magic[random.randrange(0, len(self.magic))]

        current_mp = self.get_mp()

        if spell.cost > current_mp or (spell.type == "white" and self.hp > self.max_hp // 3):
            return self.choose_enemy_spell()

        self.reduce_mp(spell.cost)

        return spell
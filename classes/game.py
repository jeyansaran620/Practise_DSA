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
    def __init__(self,hp,mp,atk,df,magic):
        self.max_hp=hp
        self.hp=hp
        self.max_mp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic

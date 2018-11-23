class Human:
    name: str = "a"
    status: str = "alive"

    def isDead(self):
        print(self.status)


class Murderer:
    name: str = "Razor"

    def __init__(self, name:str):
        self.name = name

    def kill(self,hum:Human):
        hum.status = "killed by "+ self.name


zubenko: Human = Human()
zubenko.isDead()
killer: Murderer = Murderer("Razor")
killer.kill(zubenko)
zubenko.isDead()
killer1: Murderer = Murderer("Slave")
killer1.kill(zubenko)
zubenko.isDead()

# второе задание я нихуя не понял что блять значит загрузите опенсорсору используя оопэ? ало нахуй


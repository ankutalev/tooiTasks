class Human:
    name: str = "a"
    status: str = "alive"

    def isDead(self):
        print(self.status)


class Murderer:
    name: str = "Razor"

    def __init__(self, name: str):
        self.name = name

    def kill(self, hum: Human):
        hum.status = "killed by " + self.name


man: Human = Human()
man.isDead()
killer: Murderer = Murderer("Razor")
killer.kill(man)
man.isDead()
killer1: Murderer = Murderer("Slave")
killer1.kill(man)
man.isDead()

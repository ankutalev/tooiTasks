class Figure:
    name: str
    color: str

    def info(self):
        print(self.name,self.color)
        print()


class Triangle(Figure):
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color

    def info(self):
        print("I am triangle, hi!")
        Figure.info(self)


class Circle(Figure):
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color

    def info(self):
        print("I am circle, hi!")
        Figure.info(self)


figures :[Figure] = []
figures.append(Circle("best circle","green"))
figures.append(Triangle("best triangle","yellow"))
for f in figures:
    f.info()


class TrainTravel:
    cost:int = 100500
    destintation: str = "Urupinsk"


class Human:
    money: int
    name: str

    def __init__(self,money:int, name:str):
        self.money=money
        self.name=name

    def buy_ticket(self,destination: TrainTravel):
        if self.money < destination.cost:
            print("Not enough money!")
        else:
            self.money-=destination.cost
            print(self.name, " buy ticket to ",destination.destintation, " and now has ",self.money)

city: TrainTravel = TrainTravel()
jack : Human = Human(3242,"Jack")
tina :Human = Human(100501, "Tina")
jack.buy_ticket(city)
tina.buy_ticket(city)

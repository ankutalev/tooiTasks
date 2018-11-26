
class Things:
    color: str = "white" #error fix
    total: int = 0
    namething: str = "my name"


    def __init__(self, n, t):
        self.namething = n
        self.total = t


th1 = Things("table", 5)
th2 = Things("computer", 7)
print(th1.namething, th1.total)
print(th2.namething, th2.total)
th1.color = "green"
print(th1.color)
print(th2.color)


class Table:
    long: int = 0
    width: int = 0
    height: int = 0

    def __init__(self, l:int, w:int, h:int):
        self.long = l
        self.width = w
        self.height = h

    def calc_volume(self):
        return self.height*self.width*self.long

    def info(self):
        print("I am simple table with volume", self.calc_volume())


class BestTable (Table):
    name: str = "Graham"

    def info(self):
        print("I AM BEST TABLE with VOLUME", self.calc_volume(), ' AND I GOT NAME ',self.name)


tables: [Table] = [Table(1,2,3), BestTable(1,2,3)]
for t in tables:
    t.info()


class Figure:
    color: str = "TITANIUM WHITE"

    def change_color(self, new_color: str):
        self.color = new_color

    def info(self):
        print("i am ", self.color," figure")


class Circle(Figure):
    radius: int

    def __init__(self, r: int):
        self.radius = r

    def info(self):
        print("I am ",self.color, " circle with radius ",self.radius)


class Rectangle(Figure):
    length: int
    width: int

    def __init__(self, l:int, w:int):
        self.width = w
        self.length = l

    def info(self):
        print("I am ",self.color, " rectangle with square ", self.length*self.width)


figures: [Figure] = [Figure(), Circle(12), Rectangle(312,2)]
figures[1].change_color("just white")
figures[2].change_color("also black")

for f in figures:
    f.info()

# с сотрудниками вообще тоже самое, лень копипасту делать, фантазии у меня мало, хоть я и много чего себе придумываю 


# -*- coding: utf-8 -*-


class Aricraft:
    mileages = 0.0 # 类变量，在该类及其子类的实例中共享
    def __init__(self, engine, speed):
        self.engine = engine
        self.speed = speed
    def fly(self, miles):
        Aricraft.mileages += miles
        print("the aircrift has", Aricraft.mileages, "miles")

aricraft = Aricraft("涡扇9", "800km/h")
aricraft.fly(1000)
aricraft.fly(600)

class Fighter(Aricraft): # 继承
    def __missile(self): # 私有方法，只能类内访问
        print("emission missile !")

    def fly(self, miles):
        Aricraft.mileages += miles
        print("the fighter has", Aricraft.mileages, "miles")
        Fighter.__missile(self)

fighter = Fighter("涡扇15", "1200km/h")
fighter.fly(1800)
fighter.fly(1600)

def a():
    return 1

res=a()
print(res)
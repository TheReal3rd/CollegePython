class Engine:
    running = False

class Car:
    def __init__(self, colour, make, sound):
        self.colour = colour
        self.make = make
        self.engine = Engine
        self.sound = sound
    def BlowHorn(self):
        return self.sound
    def IsEngineRunning(self):
        return self.engine.running
    def ToggleEngine(self):
        if(self.engine.running):
            self.engine.running = False
        else:
            self.engine.running = True

car1 = Car("Blue", "carMake","CarSound1")
car2 = Car("Red", "carMake1", "CarSound2")

print(car1.make)
print(car1.colour)
print(car1.IsEngineRunning())
print(car1.BlowHorn())
car1.ToggleEngine()
print(car1.IsEngineRunning())
print(car2.colour)

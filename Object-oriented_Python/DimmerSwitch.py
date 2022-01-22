class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.level = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def levelUp(self):
        if self.level < 10:
            self.level += 1

    def levelDown(self):
        if self.level > 0:
            self.level -= 1
    
    def show(self):
        print(f'Is light on?: {self.switchIsOn}')
        print(f"Dimmer's level is: {self.level}")


obj = DimmerSwitch()
obj.show()
print()
obj.turnOn()
obj.show()
print()
obj.levelUp()
obj.levelUp()
obj.show()
print()
obj.turnOff()
obj.levelDown()
obj.show()





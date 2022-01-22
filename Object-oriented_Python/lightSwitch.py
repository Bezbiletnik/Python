class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def status(self):
        return self.switchIsOn


##obj = LightSwitch()
##print(obj.status())
##obj.turnOn()
##print(obj.status())

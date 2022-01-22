from lightSwitch import *

oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

print(oLightSwitch1.status())
print(oLightSwitch2.status())
oLightSwitch1.turnOn()
print(oLightSwitch1.status())
print(oLightSwitch2.status())

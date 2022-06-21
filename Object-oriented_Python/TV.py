class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelsList = [1, 2, 3, 5, 7, 10, 15, 31]
        self.nChannels = len(self.channelsList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM

    def power(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if not self.isOn:
            return
        if newChannel in self.channelsList:
            self.channelIndex = self.channelsList.index(newChannel)

    def showInfo(self):
        print('\nTV status:')
        if self.isOn:
            print('\tTV is: On')
            print('\tChannel is:', self.channelsList[self.channelIndex])
            if self.isMuted:
                print('\tVolume is:', self.volume, '(sound is muted)')
            else:
                print('\tVolume is:', self.volume)
        else:
            print('\tTV is: Off')


obj = TV()
obj.power()
obj.showInfo()
for _ in range(3):
    obj.volumeUp()
    obj.channelUp()
obj.showInfo()
obj.volumeDown()
obj.setChannel(31)
obj.mute()
obj.showInfo()
obj.power()
obj.showInfo()

from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def show_name(self):
        print("Device:", self.name)


class SmartLight(SmartDevice):

    def turn_on(self):
        print(self.name, "is now ON. The light is bright.")

    def turn_off(self):
        print(self.name, "is now OFF.")


class SmartFan(SmartDevice):

    def turn_on(self):
        print(self.name, "is now ON. The fan is spinning.")

    def turn_off(self):
        print(self.name, "is now OFF.")


class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print(self.name, "is now ON. Playing music.")

    def turn_off(self):
        print(self.name, "is now OFF. Music stopped.")



light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
speaker = SmartSpeaker("Smart Speaker")

devices = [light, fan, speaker]

for device in devices:
    device.show_name()
    device.turn_on()
    device.turn_off()
    print()
class Animal:

    def voice(self):
        pass


class Cat(Animal):
    def speak(self):
        Animal.voice('мяу')


class Dog(Animal):
    def speak(self):
        spk = Animal.voice('гав')


class Frog(Animal):
    def speak(self):
        spk = Animal.voice('ква')


d = Cat()
d.voice()
Dog()
Frog()
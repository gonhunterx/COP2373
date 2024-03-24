class Bird:
    def __init__(self, name):
        self._name = name 

class Flamingo(Bird):
    def __init__(self, name):
        super().__init__(name)
        self.name = name 
        
bird = Bird('bird')
flamingo = Flamingo('flamingo')

print(isinstance(flamingo, Bird))
print(isinstance(flamingo, Flamingo))
#Python class

class Robot:
    def __init__(self , Name, Color, Weight):
        self.name = Name
        self.color = Color
        self.weight = Weight
    
    def introduce_self(self):
        print("My Name is " + self.name)
        print(self.name + " is " + self.color + " in color")
        print(self.name + " weighs " + self.weight)
        
r1 = Robot("Tom", "red","40")


r1.introduce_self()
    

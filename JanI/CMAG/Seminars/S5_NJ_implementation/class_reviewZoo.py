#!/usr/bin/python3

class Animal(object):

    def __init__(self, eyes, color): #when you define animal, define its eye and color
        self.eyes=eyes
        self.color=color
    
    def eye_number(self):
        return self.eyes
    
    def skin(self):
        return self.color
    
    def feeding_time(self):#we use abstract, to know that its a number n (14 for example) when its a concrete animal (we know lion is 14)
        return "time"
    #separate into feeding habits
    def food_type(self): #we use the same method as before (mistery for now) to know what it is for each class definition (lion is meat)
        return "food"

#WRONG?, class is Lion (or another animal) to define pumba=Lion(eyes, color)

class ZooKeeper(object):

    def __init__(self, kg_meat):
        self.meat=kg_meat
    #in zoo, define feeding groups
    #categorize each animal


lion=Animal(2, "brown") #we know it eats
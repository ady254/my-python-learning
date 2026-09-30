# I - Interface Segregation Principle

#Don't force classes to implement things they don't need.

#Bad:

class Worker:

    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

# Imagine:
class Robot(Worker):

#Robot doesn't need: eat(), sleep()

# Better to split interfaces:

class Workable():
    def work(self):
        pass

class Eatable(self):
    def eat(self):
        pass

#In Python, this can be expressed using Protocol particularly nicely.
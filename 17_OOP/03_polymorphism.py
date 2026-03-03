"""
Topic: Python Polymorphism
Date: 2026-03-02
Concept Covered:
- What is polymorphism?
"""
# Think of polymorphism like a TV remote - the "power" button does different things for different devices (TV, soundbar, DVD player), but you press it the same way!
# What is Polymorphism?
# Poly = many
# Morphism = forms
# So polymorphism means "many forms" - the same thing behaving differently in different situations!

# Method 1: Polymorphism with same interface
# - Different classes, same method names:

class EmailNotification:
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification:
    def send(self, message):
        print(f"Sending Push Notification: {message}")

# All notifications can be sent the same way!
def notify_all(notification_systems, message):
    for system in notification_systems:
        system.send(message)

# Set up different notification methods
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

# Send notifications
notify_all(notifications, "Hello, world!")

# Output:
# Sending email: Hello, world!
# Sending SMS: Hello, world!
# Sending Push Notification: Hello, world! 

# Method 2: Polymorphism with Inheritance
# Parent class defines the structure, children provide specifics:
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass  # Parent just says "do something"

# Child classes
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says: Meow!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says: Moo!"

# All animals have make_sound(), but each is different
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Cow("Bessie")
    
]

for animal in animals:
    print(animal.make_sound())
# Output:
# Buddy says: Woof!
# Whiskers says: Meow!
# Bessie says: Moo!


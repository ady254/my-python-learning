# L- Liskov Subsitution Priciple
# This is commonly memorized badly.

#Don't memorize:

#"Subtypes must be substitutable for their base types."

#Understand the question:

#Can I replace the parent with the child without breaking the expected behavior?
class Bird:

    def fly(self):
        pass

class Sparrow(Bird):

    def fly(self):
        print("Flying")

class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")

#Now the abstraction is wrong.

#Because the system expects:

#bird.fly()

#to work for every Bird.

# better:

class Bird:
    pass


class FlyingBird(Bird):

    def fly(self):
        pass


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass

# D — Dependency Inversion Principle
# The Dependency Inversion Principle (DIP) is a software design rule that states high-level modules should not depend on low-level modules;
# both should depend on abstractions.

#Core Rules
#• No direct ties: High-level code (business logic) should not connect directly to low-level code (database access, UI, APIs).
#• Use interfaces: Both levels must connect through an abstraction, like an interface or abstract class.
#• Details depend on abstractions: The specific inner workings must fit the rules of the abstraction, not the other way around.

#Key Benefits
#• Loose Coupling: Changing how a low-level tool works (like switching from a file logger to a database logger) requires zero changes to your core business logic.
#• Easy Testing: You can easily pass fake or mock versions of interfaces into your high-level classes during testing.


#DIP vs. Dependency Injection (DI)
#• DIP (The Principle): A high-level guideline stating that classes should rely on interfaces instead of concrete classes.
#• DI (The Technique): A coding pattern used to hand over or supply those dependent objects (via constructor or property) to a class from the outside. 
# You use Dependency Injection to help achieve the Dependency Inversion Principle.

# bad
class UserService:

    def __init__(self):
        self.db = PostgreSQLDatabase()

#now
#UserService
     ↓
#PostgreSQLDatabase

#The high-level service is tightly coupled to one implementation.

# better
class UserService:

    def __init__(self, repository):
        self.repository = repository

                # ┌── PostgreSQLRepository
                 │
#UserService ─────┼── MongoRepository
                 │
                # └── FakeRepository
# This is also where dependency injection comes in.

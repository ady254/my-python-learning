# Single Responsibility Principle:
# A class should have only one responsibility
# Aclass should not be responsible for multiple responsibilities

# BAD EXAMPLE: one class does validation, persistence, and email sending
class User:
      def register(self, data):
            if "@" not in data["email"]:    
                 raise ValueError("bad email")
            db.save(data)
           send_email(data["email"], "Welcome!") # violation of SRP
    
# GOOD EXAMPLE: SPLIT THE RESPONSIBILITIES INTO SEPARATE CLASSES
class UserValidation:
    def validate(self, data):

class UserRespository:
    def save(self, user):

class WelcomeEmail:
    def send(self, email):


# A Simple Real-World Analogy
# Imagine a small restaurant with one employee who acts as the Chef, the Waiter, and the Accountant:
#  - If the **menu** changes, they have to change how they work.
# If the **seating rules** change, they have to change how they work.
# If the **tax laws** change, they have to change how they work.

# That single person has **three different reasons to change**. If they make a mistake calculating taxes, the kitchen comes to a halt!


# why it matters:
# 1. It makes it easier to understand the code
# 2. It makes it easier to maintain the code
# 3. It makes it easier to test the code
# 4. It makes it easier to refactor the code
# 5. It makes it easier to deploy the code
# 6. It makes it easier to scale the code
# 7. It makes it easier to debug the code
# 8. It makes it easier to document the code
# 9. It makes it easier to reuse the code
   
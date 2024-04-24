# como rodar --> python3 class.py (no terminal)


class Dog:
    """The __init__() method is a special method that Python runs automatically
    whenever we create a new instance based on the Dog class. The self
    parameter is required in the method definition, and it must come first,
    before the other parameters."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")


# my_dog = Dog("Ruby", 3)

# my_dog.sit()
# print(my_dog.age)


# Exercicios

""" Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods."""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"O restourante {self.restaurant_name} faz comida {self.cuisine_type}")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name} está aberto")


# rest_1 = Restaurant("lulu", "Arabe")

# rest_1.describe_restaurant()
# rest_1.open_restaurant()


""" Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the users information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both meth-
ods for each user. Add an attribute called login_attempts to your User class.
Add an attribute called login_attempts to your User class. Write a method called
increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of
login_attempts to 0. """


class User:
    def __init__(self, first_name, last_name):
        self.user_information = {}
        self.user_information["first_name"] = first_name
        self.user_information["last_name"] = last_name
        self.login_attempts = 0

    def describe_user(self, **user_information):
        for key in user_information.keys():
            self.user_information[key] = user_information[key]

        return self.user_information

    def greet_user(self):
        print(f"Olá {self.user_information['first_name']}, tudo bem?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# user_1 = User("Jessica", "Arruda")
# user_1.describe_user(pet="Ruby", age=32)
# user_1.greet_user()

# user_1.increment_login_attempts()
# print(user_1.login_attempts)

# user_1.reset_login_attempts()
# print(user_1.login_attempts)


# Inheritance - exercicios


""" Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class. Add an attribute, privileges, that
stores a list of strings like "can add post", "can delete post", "can ban user",
and so on. Write a method called show_privileges() that lists the administrator's
set of privileges. Create an instance of Admin, and call your method.
"""

""" Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings. Move the show_privileges()
method to this class. Make a Privileges instance as an attribute in the Admin 
class. Create a new instance of Admin and use your method to show its privileges. 
"""


class Privileges:
    def __init__(self, privileges=["add post", "delete post", "ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        return self.privileges

    def add_privilege(self, privilege: str):
        if privilege:
            self.privileges.append(privilege)
            return self.privileges

        return self.privileges


class Admin(User):
    def __init__(
        self, first_name, last_name, privileges=Privileges().add_privilege("")
    ):
        super().__init__(first_name, last_name)
        self.user_information["privileges"] = privileges

    def print_information_admin(self, *information):
        if information:
            for item in information:
                print(f"{item}: {self.user_information[item]}")
        else:
            for item in self.user_information:

                print(f"{item}: {self.user_information[item]}")

    def add_admin_privileges(self, *privileges: str):
        for item in privileges:
            self.user_information["privileges"].append(item)


admin_1 = Admin("Jessica", "Arruda")
admin_1.add_admin_privileges("list all posts", "add friends")
admin_1.describe_user(age=32)
admin_1.print_information_admin()

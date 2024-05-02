from pathlib import Path
import json


# cria um arquivo json contendo o array passado, para cada vez que o codigo for rodado
# o arquivo criado é sobrescrito

numbers = [2, 3, 5, 6, 8, 10]

# path = Path("numbers.json")
# contents = json.dumps(numbers)
# path.write_text(contents)

# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)
# print(numbers)


class Json_User_Crud:
    def __init__(self, username):
        self.user_information = {}
        self.user_information["username"] = username
        self.path = Path(f"{username}.json")

    def add_user_information(self, **information):
        if not self.path.exists():
            for key in information.keys():
                self.user_information[key] = information[key]

            self.path.write_text(json.dumps(self.user_information))

    def read_user_information(self, *information):
        permitted_information_list = [
            "Full_name",
            "Date_of_birth",
            "Gender",
            "Email_address",
        ]
        permitted_information = {}

        json_user_information = json.loads(self.path.read_text())

        if information:
            for item in information:
                if information in json_user_information:
                    permitted_information[item] = self.user_information[item]
        else:
            for item in permitted_information_list:
                permitted_information[item] = json_user_information[item]

        return permitted_information

    def updated_user_infomation(self, **information):
        if self.path.exists():
            contents = json.loads(self.path.read_text())

            for key in information.keys():
                if key in contents:
                    contents[key] = information[key]

            self.path.write_text(json.dumps(contents))

    def delete_user_information(self, **infomation):
        if self.path.exists():
            contents = json.loads(self.path.read_text())

            for key in infomation.keys():
                if key in contents and key in self.user_information:
                    self.user_information[key] = ""
                    contents[key] = ""

            self.path.write_text(json.dumps(contents))


user_1 = Json_User_Crud("johndoe123")

user_1.add_user_information(
    Full_name="John Doe",
    Date_of_birth="1985-07-15",
    Gender="Male",
    Email_address="john.doe@example.com",
    Phone_number="+1234567890",
    Physical_address="123 Main Street, Cityville, USA",
    Identification_document="Driver's License - 123456789",
    Username="johndoe123",
    Password="hashed_password_here",
    Credit_card_details="**** **** **** 1234",
    Billing_address="123 Billing Lane, Cityville, USA",
    Transaction_history="2024-04-29: $50.00 at Store A",
)

print(user_1.read_user_information())

user_1.updated_user_infomation(Date_of_birth="1999-07-15",Full_name='Jonathan Doe')

print(user_1.read_user_information())
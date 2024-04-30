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


class Json_crud:
    def __init__(self, username):
        self.user_information = {}
        self.user_information["username"] = username
        self.path = Path(f'{username}.json')

    def add_user_information(self, **information):
        if not self.path.exists(): 
            for key in information.keys():
                self.user_information[key] = information[key]

            self.path.write_text(json.dumps(self.user_information))

    def read_user_information(self, *information):
        permitted_information_list = [
            "name",
            "last_name",
            "age",
            "username",
            "pet",
            "job",
            "education",
            "gender",
            "email",
        ]
        permitted_information = {}
  
        json_user_information= json.loads(self.path.read_text())

        if information:
            for item in information:
                if information in json_user_information:
                    permitted_information[item] = self.user_information[item]
        else:
            for item in permitted_information_list:
                permitted_information[item] = json_user_information[item]
        
        return permitted_information

    def updated_user_infomation(self, username, *information,):
        if self.path.exists():
            for key in information.keys():
                if key in self.user_information:
                    self.user_information[key] = information[key]
    
    def delete_user_information(self, *infomation):
        for key in infomation.keys():
            if key in self.user_information:
                self.user_information[key] = ""

import datetime


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created: datetime = datetime.datetime.now()

    def is_active(self) -> bool:
        send_time = datetime.datetime.now()
        return self.created + self.deadline > send_time


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework) -> object:
        if homework.is_active():
            return homework
        print("You are late")


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

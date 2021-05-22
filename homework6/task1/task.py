import datetime
from collections import defaultdict


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
        super().__init__(self.message)


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

    def do_homework(self, homework: Homework, solution) -> object:
        student = Student.__call__(self.last_name, self.first_name)
        if homework.is_active():
            return HomeworkResult(homework, student, solution)
        raise DeadlineError


class HomeworkResult:
    def __init__(self, homework, student, solution: str):
        if not isinstance(homework, Homework):
            raise AttributeError("Class passing error")
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.datetime.now()


class Teacher(Student):
    homework_done = defaultdict(list)
    _homework_done_details = defaultdict(list)

    def create_homework(self, text, deadline):
        return Homework(text, deadline)

    def check_duplicate_homework(self, homework_result):
        author_full_name = (
            f"{homework_result.author.first_name} {homework_result.author.last_name}"
        )
        homework_info = (
            author_full_name,
            homework_result.solution,
            homework_result.homework.text,
        )
        if self._homework_done_details[homework_result.homework]:
            for homework in self._homework_done_details[homework_result.homework]:
                if homework_info[0] == homework[0] or homework_info[1] == homework[1]:
                    return False
        self._homework_done_details[homework_result.homework].append(homework_info)
        return True

    def check_homework(self, homework_result):
        if len(homework_result.solution) > 5 and self.check_duplicate_homework(
            homework_result
        ):
            self.homework_done[homework_result.homework].append(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, **kwargs):
        if not kwargs:
            cls.homework_done = defaultdict(list)
            cls._homework_done_details = defaultdict(list)
        else:
            key = list(kwargs.keys())[0]
            del cls.homework_done[kwargs[key]]
            del cls._homework_done_details[kwargs[key]]

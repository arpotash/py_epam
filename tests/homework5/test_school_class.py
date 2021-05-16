import datetime
from unittest.mock import Mock

import pytest

from homework5.task1.task import Homework, Student, Teacher


class TestStudent:
    @pytest.fixture
    def get_student(self):
        return Student("Smirnov", "Daniil")

    def test_positive_firstname_lastname(self, get_student):
        """Testing right student's firstname, lastname"""
        assert get_student.first_name == "Daniil"
        assert get_student.last_name == "Smirnov"

    def test_wrong_position_arguments(self, get_student):
        """Testing wrong position student's firstname, lastname"""
        student = Student("Daniil", "Smirnov")
        assert student.first_name != "Daniil"
        assert student.last_name != "Smirnov"

    def test_do_homework_with_deadline_expired_0(self, capsys, get_student):
        """Testing that the function with deadline equal 0 prints message 'You are late'
        and returns None object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", 0))
        assert get_student.do_homework(teacher.create_homework()) is None
        out, err = capsys.readouterr()
        assert out == "You are late\n"

    def test_do_homework_with_negative_deadline(self, capsys, get_student):
        """Testing that the function with expired deadline prints message 'You are late'
        and return None object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", -2))
        assert get_student.do_homework(teacher.create_homework()) is None
        out, err = capsys.readouterr()
        assert out == "You are late\n"

    def test_do_homework_with_active_deadline(self, get_student):
        """Testing that function with active deadline returns Homework object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", 3))
        do_homework = get_student.do_homework(teacher.create_homework())
        assert teacher.create_homework() == do_homework


class TestTeacher:
    @pytest.fixture
    def get_teacher(self):
        return Teacher("Petrov", "Roman")

    def test_positive_firstname_last_name(self, get_teacher):
        """Testing right teacher's firstname, lastname"""
        assert get_teacher.first_name == "Roman"
        assert get_teacher.last_name == "Petrov"

    def test_wrong_position_argument(self):
        """Testing wrong teacher's firstname, lastname"""
        teacher = Teacher("Roman", "Petrov")
        assert teacher.first_name != "Roman"
        assert teacher.last_name != "Petrov"

    def test_create_homework_with_positive_deadline(self, get_teacher):
        """Testing right creating homework by teacher with positive deadline"""
        create_homework = get_teacher.create_homework("Create oop script", 3)
        assert create_homework.deadline == datetime.timedelta(3)
        assert create_homework.text == "Create oop script"

    def test_create_homework_with_deadline_0(self, get_teacher):
        """Testing right creating homework by teacher with deadline equal 0"""
        create_homework = get_teacher.create_homework("Create oop script", 0)
        assert create_homework.deadline == datetime.timedelta(0)
        assert create_homework.text == "Create oop script"

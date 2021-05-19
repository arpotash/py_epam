import datetime
from unittest.mock import Mock

import pytest

from homework6.task1.task import (DeadlineError, Homework, HomeworkResult,
                                  Student, Teacher)


class TestSchoolStudent:
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

    def test_do_homework_with_deadline_expired_0(self, get_student):
        """Testing that the function with deadline equal 0 prints message 'You are late'
        and returns None object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", 0))
        with pytest.raises(DeadlineError) as e:
            get_student.do_homework(teacher.create_homework(), "Solution")
            msg = e.value.args[0]
            assert msg == "You are late"

    def test_do_homework_with_negative_deadline(self, get_student):
        """Testing that the function with expired deadline prints message 'You are late'
        and return None object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", -2))
        with pytest.raises(DeadlineError) as e:
            get_student.do_homework(teacher.create_homework(), "Solution")
            msg = e.value.args[0]
            assert msg == "You are late"

    def test_do_homework_with_active_deadline(self, get_student):
        """Testing that function with active deadline returns HomeworkResult object"""
        teacher = Mock()
        teacher.create_homework = Mock(return_value=Homework("Task", 3))
        do_homework = get_student.do_homework(teacher.create_homework(), "Solution")
        assert isinstance(do_homework, HomeworkResult)
        assert do_homework.homework.text == "Task"
        assert do_homework.author.first_name == "Daniil"
        assert do_homework.author.last_name == "Smirnov"
        assert do_homework.solution == "Solution"
        assert do_homework.homework.deadline == datetime.timedelta(days=3)


class TestSchoolTeacher:
    @pytest.fixture
    def get_teacher(self):
        return Teacher("Petrov", "Roman")

    @pytest.fixture
    def get_student(self):
        return Student("Smirnov", "Daniil")

    def test_positive_firstname_last_name(self, get_teacher):
        """Testing right teacher's firstname, lastname"""
        assert get_teacher.first_name == "Roman"
        assert get_teacher.last_name == "Petrov"

    def test_wrong_position_argument(self):
        """Testing wrong teacher's firstname, lastname"""
        teacher = Teacher("Roman", "Petrov")
        assert teacher.first_name != "Roman"
        assert teacher.last_name != "Petrov"

    def test_create_homework_with_positive_deadline(self, get_teacher, get_student):
        """Testing right creating homework by teacher with positive deadline"""
        create_homework = get_teacher.create_homework("Create oop script", 3)
        assert create_homework.deadline == datetime.timedelta(3)
        assert create_homework.text == "Create oop script"

    def test_create_homework_with_deadline_0(self, get_teacher):
        """Testing right creating homework by teacher with deadline equal 0"""
        create_homework = get_teacher.create_homework("Create oop script", 0)
        assert create_homework.deadline == datetime.timedelta(0)
        assert create_homework.text == "Create oop script"

    def test_check_homework_with_right_solution(self, get_teacher, get_student):
        """Testing checking done homework by teacher with right solution"""
        create_homework = get_teacher.create_homework("Create opp hm", 3)
        done_homework = get_student.do_homework(create_homework, "Solution")
        check_result = get_teacher.check_homework(done_homework)
        assert check_result
        assert len(Teacher.homework_done[create_homework]) == 1

    def test_check_homework_with_wrong_solution(self, get_student, get_teacher):
        """Testing checking done homework by teacher with wrong solution"""
        create_homework = get_teacher.create_homework("Create opp hm", 3)
        done_homework = get_student.do_homework(create_homework, "No")
        check_result = get_teacher.check_homework(done_homework)
        assert not check_result

    def test_check_homework_with_duplicate_author(self, get_teacher, get_student):
        """Testing checking done homework from student, who has already sent the solution
        for checking"""
        create_homework = get_teacher.create_homework("Create opp hm", 3)
        done_homework = get_student.do_homework(create_homework, "I've done")
        done_homework_repeat = get_student.do_homework(create_homework, "Finished")
        check_result = get_teacher.check_homework(done_homework)
        check_result_repeat = get_teacher.check_homework(done_homework_repeat)
        assert check_result
        assert len(get_teacher.homework_done[create_homework]) == 1
        assert not check_result_repeat
        assert len(get_teacher.homework_done[create_homework]) == 1

    def test_check_homework_with_duplicate_solution(self, get_teacher, get_student):
        """Testing checking done homework with the same solutions one homework"""
        student = Student("Romanov", "Alex")
        create_homework = get_teacher.create_homework("Create opp hm", 3)
        done_homework = get_student.do_homework(create_homework, "I've done")
        done_homework_repeat = student.do_homework(create_homework, "I've done")
        check_result = get_teacher.check_homework(done_homework)
        check_result_repeat = get_teacher.check_homework(done_homework_repeat)
        assert check_result
        assert len(get_teacher.homework_done[create_homework]) == 1
        assert not check_result_repeat
        assert len(get_teacher.homework_done[create_homework]) == 1

    def test_single_homework_results_for_teachers(self, get_teacher, get_student):
        """Testing the same access to homework for all teachers"""
        teacher = Teacher("Malakhov", "Roman")
        student = Student("Romanov", "Alex")
        create_homework = get_teacher.create_homework("Create opp hm", 3)
        done_homework = get_student.do_homework(create_homework, "I've done")
        done_homework_repeat = student.do_homework(create_homework, "Finished")
        get_teacher.check_homework(done_homework)
        get_teacher.check_homework(done_homework_repeat)
        assert len(get_teacher.homework_done[create_homework]) == 2
        assert len(teacher.homework_done[create_homework]) == 2
        assert len(Teacher.homework_done[create_homework]) == 2

    def test_reset_results_all(self, get_teacher, get_student):
        """Testing reset all homework results by teacher"""
        student = Student("Romanov", "Alex")
        create_homework = get_teacher.create_homework("Create script", 2)
        create_homework_2 = get_teacher.create_homework("Create web site", 3)
        solution_1 = get_student.do_homework(create_homework, "Solution")
        solution_2 = student.do_homework(create_homework_2, "I've done")
        get_teacher.check_homework(solution_1)
        get_teacher.check_homework(solution_2)
        assert len(get_teacher.homework_done[create_homework]) == 1
        assert len(get_teacher.homework_done[create_homework_2]) == 1
        get_teacher.reset_results()
        assert get_teacher.homework_done == {}

    def test_reset_results_homework(self, get_teacher, get_student):
        """Testing reset homework results by key which is homework by teacher"""
        student = Student("Romanov", "Alex")
        create_homework = get_teacher.create_homework("Create script", 2)
        create_homework_2 = get_teacher.create_homework("Create web site", 3)
        solution_1 = get_student.do_homework(create_homework, "Solution")
        solution_2 = student.do_homework(create_homework_2, "I've done")
        get_teacher.check_homework(solution_1)
        get_teacher.check_homework(solution_2)
        assert len(get_teacher.homework_done[create_homework]) == 1
        assert len(get_teacher.homework_done[create_homework_2]) == 1
        get_teacher.reset_results(homework=create_homework)
        assert get_teacher.homework_done[create_homework] == []
        assert len(get_teacher.homework_done[create_homework_2]) == 1

    def test_create_homework_result_with_wrong_class(self, get_student):
        """Testing creating homework with wrong class when initializing attributes"""
        with pytest.raises(AttributeError) as e:
            HomeworkResult(get_student, get_student, "Solution")
            msg = e.value.args[0]
            assert msg == "Class passing error"

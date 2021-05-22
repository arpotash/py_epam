import datetime

import pytest

from homework6.task1 import task

STUDENT = task.Student("Smirnov", "Daniil")
TEACHER = task.Teacher("Petrov", "Roman")
HOMEWORK = task.Homework("Create script", 3)
HOMEWORK_WITH_EXPIRED_DEADLINE = task.Homework("Create script", 0)
HOMEWORK_WITH_NEGATIVE_DEADLINE = task.Homework("Create script", -2)
HOMEWORK_RESULT = task.HomeworkResult(HOMEWORK, STUDENT, "Solution")


class TestSchoolStudent:
    def test_positive_firstname_lastname(self):
        """Testing right student's firstname, lastname"""
        assert STUDENT.first_name == "Daniil"
        assert STUDENT.last_name == "Smirnov"

    def test_wrong_position_arguments(self):
        """Testing wrong position student's firstname, lastname"""
        student = task.Student("Daniil", "Smirnov")
        assert student.first_name != "Daniil"
        assert student.last_name != "Smirnov"

    def test_do_homework_with_deadline_expired_0(self):
        """Testing that the function with deadline equal 0 prints message 'You are late'
        and returns None object"""
        with pytest.raises(task.DeadlineError) as e:
            STUDENT.do_homework(HOMEWORK_WITH_EXPIRED_DEADLINE, "Solution")
            msg = e.value.args[0]
            assert msg == "You are late"

    def test_do_homework_with_negative_deadline(self):
        """Testing that the function with expired deadline prints message 'You are late'
        and return None object"""
        with pytest.raises(task.DeadlineError) as e:
            STUDENT.do_homework(HOMEWORK_WITH_NEGATIVE_DEADLINE, "Solution")
            msg = e.value.args[0]
            assert msg == "You are late"

    def test_do_homework_with_active_deadline(self):
        """Testing that function with active deadline returns HomeworkResult object"""
        do_homework = STUDENT.do_homework(HOMEWORK, "Solution")
        assert isinstance(do_homework, task.HomeworkResult)
        assert do_homework.homework.text == "Create script"
        assert do_homework.author.first_name == "Daniil"
        assert do_homework.author.last_name == "Smirnov"
        assert do_homework.solution == "Solution"
        assert do_homework.homework.deadline == datetime.timedelta(days=3)


class TestSchoolTeacher:
    def test_positive_firstname_last_name(self):
        """Testing right teacher's firstname, lastname"""
        assert TEACHER.first_name == "Roman"
        assert TEACHER.last_name == "Petrov"

    def test_wrong_position_argument(self):
        """Testing wrong teacher's firstname, lastname"""
        teacher = task.Teacher("Roman", "Petrov")
        assert teacher.first_name != "Roman"
        assert teacher.last_name != "Petrov"

    def test_create_homework_with_positive_deadline(self):
        """Testing right creating homework by teacher with positive deadline"""
        create_homework = TEACHER.create_homework("Create oop script", 3)
        assert create_homework.deadline == datetime.timedelta(3)
        assert create_homework.text == "Create oop script"

    def test_create_homework_with_deadline_0(self, get_teacher):
        """Testing right creating homework by teacher with deadline equal 0"""
        create_homework = get_teacher.create_homework("Create oop script", 0)
        assert create_homework.deadline == datetime.timedelta(0)
        assert create_homework.text == "Create oop script"

    def test_check_homework_with_right_solution(self):
        """Testing checking done homework by teacher with right solution"""
        check_result = TEACHER.check_homework(HOMEWORK_RESULT)
        assert check_result
        assert len(task.Teacher.homework_done[HOMEWORK]) == 1

    def test_check_homework_with_wrong_solution(self):
        """Testing checking done homework by teacher with wrong solution"""
        done_homework = STUDENT.do_homework(HOMEWORK, "No")
        check_result = TEACHER.check_homework(done_homework)
        assert not check_result

    def test_check_homework_with_duplicate_author(self):
        """Testing checking done homework from student, who has already sent the solution
        for checking"""
        done_homework_repeat = STUDENT.do_homework(HOMEWORK, "Finished")
        check_result = TEACHER.check_homework(HOMEWORK_RESULT)
        check_result_repeat = TEACHER.check_homework(done_homework_repeat)
        assert check_result
        assert len(TEACHER.homework_done[HOMEWORK]) == 1
        assert not check_result_repeat
        assert len(TEACHER.homework_done[HOMEWORK]) == 1

    def test_check_homework_with_duplicate_solution(self):
        """Testing checking done homework with the same solutions one homework"""
        student = task.Student("Romanov", "Alex")
        done_homework_repeat = student.do_homework(HOMEWORK, "Solution")
        check_result = TEACHER.check_homework(HOMEWORK_RESULT)
        check_result_repeat = TEACHER.check_homework(done_homework_repeat)
        assert check_result
        assert len(TEACHER.homework_done[HOMEWORK]) == 1
        assert not check_result_repeat
        assert len(TEACHER.homework_done[HOMEWORK]) == 1

    def test_single_homework_results_for_teachers(self):
        """Testing the same access to homework for all teachers"""
        teacher = task.Teacher("Malakhov", "Roman")
        student = task.Student("Romanov", "Alex")
        done_homework_repeat = student.do_homework(HOMEWORK, "Finished")
        TEACHER.check_homework(HOMEWORK_RESULT)
        TEACHER.check_homework(done_homework_repeat)
        assert len(TEACHER.homework_done[HOMEWORK]) == 2
        assert len(teacher.homework_done[HOMEWORK]) == 2
        assert len(task.Teacher.homework_done[HOMEWORK]) == 2

    def test_reset_results_all(self):
        """Testing reset all homework results by teacher"""
        student = task.Student("Romanov", "Alex")
        create_homework_2 = TEACHER.create_homework("Create web site", 3)
        solution_2 = student.do_homework(create_homework_2, "I've done")
        TEACHER.check_homework(HOMEWORK_RESULT)
        TEACHER.check_homework(solution_2)
        assert len(TEACHER.homework_done[HOMEWORK]) == 1
        assert len(TEACHER.homework_done[create_homework_2]) == 1
        TEACHER.reset_results()
        assert TEACHER.homework_done == {}

    def test_reset_results_homework(self):
        """Testing reset homework results by key which is homework by teacher"""
        student = task.Student("Romanov", "Alex")
        create_homework_2 = TEACHER.create_homework("Create web site", 3)
        solution_2 = student.do_homework(create_homework_2, "I've done")
        TEACHER.check_homework(HOMEWORK_RESULT)
        TEACHER.check_homework(solution_2)
        assert len(TEACHER.homework_done[HOMEWORK]) == 1
        assert len(TEACHER.homework_done[create_homework_2]) == 1
        TEACHER.reset_results(homework=HOMEWORK)
        assert TEACHER.homework_done[HOMEWORK] == []
        assert len(TEACHER.homework_done[create_homework_2]) == 1

    def test_create_homework_result_with_wrong_class(self):
        """Testing creating homework with wrong class when initializing attributes"""
        with pytest.raises(AttributeError) as e:
            task.HomeworkResult(STUDENT, STUDENT, "Solution")
            msg = e.value.args[0]
            assert msg == "Class passing error"

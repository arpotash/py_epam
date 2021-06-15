import datetime
from django.test import TestCase
from .models import Student, Teacher, Homework, HomeworkResult
from django_test_migrations.migrator import Migrator


class TestMigrations(TestCase):

    migrator = Migrator(database='default')

    def test_main_migrations_0002(self):
        old_state = self.migrator.apply_initial_migration(('mainapp', '0001_initial'))
        student = old_state.apps.get_model('mainapp', 'Student')
        self.assertEqual(student.objects.count(), 0)
        new_state = self.migrator.apply_tested_migration(('mainapp', '0002_auto_20210608_1526'))
        student = new_state.apps.get_model('mainapp', 'Student')
        self.assertEqual(student.objects.count(), 5)


class TestModels(TestCase):

    def setUp(self) -> None:
        self.student = Student.objects.create(first_name='student_first_name',
                                              last_name='student_last_name')
        self.teacher = Teacher.objects.create(first_name='teacher_first_name',
                                              last_name='teacher_last_name')
        self.homework = Homework.objects.create(teacher=self.teacher, text='homework text',
                                                deadline=datetime.timedelta(days=1))

    def test_student_model(self):
        self.assertEqual(self.student.first_name, 'student_first_name')
        self.assertEqual(self.student.last_name, 'student_last_name')

    def test_teacher_model(self):
        self.assertEqual(self.teacher.first_name, 'teacher_first_name')
        self.assertEqual(self.teacher.last_name, 'teacher_last_name')

    def test_homework_model(self):
        self.assertEqual(self.homework.text, 'homework text')
        self.assertEqual(self.homework.deadline, datetime.timedelta(days=1))
        self.assertEqual(self.homework.teacher.first_name, 'teacher_first_name')
        self.assertEqual(self.homework.teacher.last_name, 'teacher_last_name')

    def test_homework_result_model(self):
        self.homework_result = HomeworkResult.objects.create(student=self.student,
                                                             homework=self.homework,
                                                             solution='solution')
        self.assertEqual(self.homework_result.student.first_name, 'student_first_name')
        self.assertEqual(self.homework_result.student.last_name, 'student_last_name')
        self.assertEqual(self.homework_result.homework.text, 'homework text')
        self.assertEqual(self.homework_result.homework.deadline, datetime.timedelta(days=1))
        self.assertEqual(self.homework_result.homework.teacher.first_name, 'teacher_first_name')
        self.assertEqual(self.homework_result.homework.teacher.last_name, 'teacher_last_name')
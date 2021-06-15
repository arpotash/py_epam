from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    class Meta:
        unique_together = [['first_name', 'last_name']]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        unique_together = [['first_name', 'last_name']]


class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    text = models.TextField(unique=True)
    deadline = models.DurationField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Homework: {self.text}'


class HomeworkResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_index=True)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, db_index=True)
    solution = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.homework} {self.student}'

    class Meta:
        unique_together = [['student', 'homework'], ['homework', 'solution']]

    def save(self, *args, **kwargs):
        if len(self.solution) < 5:
            raise ValueError("Solution should be more than 5 symbols")
        super(HomeworkResult, self).save(*args, **kwargs)
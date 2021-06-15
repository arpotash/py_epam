from django.core.management.base import BaseCommand
from mainapp.models import HomeworkResult
import csv


class Command(BaseCommand):
    help = 'Download homework results into csv file'

    def handle(self, *args, **options):

        homework_results = HomeworkResult.objects.all()
        with open('report.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(["Student", "Created", "Teacher"])
            for line in homework_results:
                writer.writerow([line.student, line.homework.created, line.homework.teacher])

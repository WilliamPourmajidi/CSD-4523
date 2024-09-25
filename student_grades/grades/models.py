# grades/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    grade1 = models.FloatField()
    grade2 = models.FloatField()
    grade3 = models.FloatField()
    grade4 = models.FloatField()

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3 + self.grade4) / 4


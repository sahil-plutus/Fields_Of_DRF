from django.db import models

GENDER = (
    ('Boy', 'Boy'),
    ('Girl', 'Girl'),
)


class Student(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    url = models.URLField(max_length=122)
    gender = models.CharField(choices=GENDER, max_length=4)
    marks = models.IntegerField()

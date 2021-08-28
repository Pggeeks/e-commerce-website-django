from django.core import validators
from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator , MinValueValidator
from courses.models import Course
from django.contrib.auth.models import User

class  Comment(models.Model):
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="comments",)
    Name = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=15)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
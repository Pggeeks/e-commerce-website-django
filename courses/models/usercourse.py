from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import BooleanField
from courses.models.coursemod import Course
from django.contrib.auth.models import User
class user_course(models.Model):
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.user.username}-{self.course.cname}'
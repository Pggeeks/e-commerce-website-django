import courses
from django.db import models
from django.db.models.fields import BooleanField
from courses.models import Course, user_course
from django.contrib.auth.models import User


class payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50, null=True, blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user_course = models.ForeignKey(
        user_course, null=True, on_delete=models.CASCADE,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}-{self.course.cname}'

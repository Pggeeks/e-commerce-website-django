from django.db import models
from django.db.models.fields import BooleanField
from courses.models import Course
from django.contrib.auth.models import User
class vid(models.Model):
    title = models.CharField(max_length=20, default="")
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE, default="")
    serial_num=models.IntegerField(null=False)
    vid_id=models.CharField(max_length=80,null=True)
    is_preview=BooleanField(default=False)
    
    def __str__(self):
        return self.title
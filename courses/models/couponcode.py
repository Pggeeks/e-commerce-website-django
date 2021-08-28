from django.core import validators
from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator , MinValueValidator
from courses.models import Course

class Coupon(models.Model):
    coupon_name= models.CharField(max_length=15, null=False)
    coupon_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField() 
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = BooleanField()
    def __str__(self):
        return self.coupon_name
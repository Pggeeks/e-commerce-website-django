from django.db import models
from django.db.models.fields.related import ForeignKey


class Course(models.Model):
    cname = models.CharField(max_length=30, null=False, default="")
    slug = models.SlugField(max_length=50, null=False , unique=True)
    cdesc = models.CharField(max_length=200, null=True, default="")
    cprice = models.IntegerField(null=False)
    cdiscount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    cthumbnail = models.ImageField(upload_to="files/thumbnail")
    pubdate = models.DateTimeField(auto_now=True)
    clength = models.IntegerField(null=False)
    resorces = models.FileField(upload_to='files/resources')

    def __str__(self):
        return self.cname


class courseProperty(models.Model):
    id = models.AutoField(primary_key=True) 
    description = models.CharField(max_length=20, default="")
    course = models.ForeignKey(
        Course, null=False, on_delete=models.CASCADE, default="")

    class Meta:
        abstract = True


class tag(courseProperty):
    pass


class Prerequisite(courseProperty):
    pass


class learning(courseProperty):
    pass

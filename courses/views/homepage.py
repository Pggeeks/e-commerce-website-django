from courses.models.usercourse import user_course
from django.shortcuts import render
from courses.models import Course
from django.shortcuts import HttpResponse
from django.template import Context, Template, context
from courses.models import user_course
from django.views.generic.list import ListView
# Create your views here.
class HomePage(ListView):
    template_name='courses/index.html'
    context_object_name = 'allcourse'
    def get_queryset(self):
        return Course.objects.all()
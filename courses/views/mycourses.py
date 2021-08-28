from os import name
from django.contrib.auth import login
from courses.models.usercourse import user_course
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
# 1 method
'''
@login_required(login_url="login")
@csrf_protect
def my_courses(request):
    user = request.user
    mycourses=user_course.objects.filter(user = user)
    return render(request,'courses/mycourses.html',context={"mycourses":mycourses})
''' 

# 2 method
@method_decorator(login_required(login_url='login'), name='dispatch')
class Mycourseslist(ListView):
    template_name='courses/mycourses.html'
    context_object_name = 'mycourses'
    def get_queryset(self):
        print(self.request.session.get('user'))
        return user_course.objects.filter(user = self.request.user)
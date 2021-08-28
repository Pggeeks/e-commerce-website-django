import courses
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from courses.models import Course
def results(request):
    result = None
    if request.method == 'POST':
        searched = request.POST['searched_data']
        try:
            result = Course.objects.get(cname__contains=searched)
            print(result)
        except:
            result = None
    return render(request,template_name="courses/search_results.html",context={"searchresult":result,"searched":searched})
from os import name

from courses import views
from courses.models.coursemod import Course
from courses.views import Mycourseslist, checkout
from courses.views.checkout import verify_payment
from courses.views.mycourses import Mycourseslist
from courses.views.search import results
from courses.views.showpage import playvideo
from courses.views.signup_login import LoginView, SignupView, signout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.urls.conf import include
from django.views.static import serve

from cwp.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin', admin.site.urls),
    path("",include('courses.urls')),
 ]


from courses.forms.loginform import *
from courses.forms.registration import Register
from django import forms, template
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.forms import ValidationError
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context, Template, context
from django.views import View
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'courses/signup.html'
    form_class = Register
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user_login = authenticate(username=username, password=raw_password)
        auth_login(self.request, user_login)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'courses/login.html'
    form_class = loginf
    success_url = '/'

    def form_valid(self, form):
        auth_login(self.request, form.cleaned_data)
        self.request.session['user'] = form.cleaned_data.email
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)


# long method for authentication
'''
class SignupView(View):
    def get(self,request):
            form = Register ()
            return render(request,template_name='courses/signup.html',context={'form':form})
    def post(self,request):
        form = Register(request.POST)
        if (form.is_valid()):
            user_data = form.save()
            username=form.cleaned_data['username']
            raw_password=form.cleaned_data['password1']
            user_login = authenticate(username=username, password=raw_password)
            auth_login(request, user_login)
            return redirect('/')
        return render(request,template_name='courses/signup.html',context={'form':form})
'''

'''
class LoginView(View):
    def get(self, request):
        form = loginf()
        print(request.user)
        print('get')
        return render(request, template_name='courses/login.html', context={'form': form})

    def post(self, request):
        form = loginf(request=request, data=request.POST)
        print('post')
        if (form.is_valid()):
            print(request.user)
            return redirect('/')
        return render(request, template_name='courses/login.html', context={'form': form})

'''


def signout(request):
    logout(request)
    return redirect('/')

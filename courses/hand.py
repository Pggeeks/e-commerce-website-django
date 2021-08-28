from django.shortcuts import redirect,render
def error_404(request,exception):
    return redirect('/')
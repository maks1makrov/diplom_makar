from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from classroom.models import Materials


class ShowAll(View):

    def get(self, request):
        if request.user.is_authenticated:
            response = {}
            response['materials'] = Materials.objects.all()
            return render(request, "show_all.html", response)
        else:
            return redirect("login")


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'log_in.html', {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('show_all')
        messages.error(request, message="login or password is not correct")
        return redirect('login')

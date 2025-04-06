from django.shortcuts import render, redirect
from utils.utils import POST_STR
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == POST_STR:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('login')
        else:
            print(form.cleaned_data)
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def account_home(request):
    return render(request, 'users/base.html', {})

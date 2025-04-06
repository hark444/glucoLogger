import logging
from utils.utils import POST_STR
from django.contrib import messages
from .forms import UserProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .template_registries import (
    USER_REGISTRATION_TEMPLATE, USER_BASE_TEMPLATE, USER_LOGIN_TEMPLATE, USER_PROFILE_UPDATE_TEMPLATE
)


logger = logging.getLogger(__name__)


@login_required(login_url="/accounts/login")
def account_home(request):
    messages.add_message(request, messages.INFO, "Welcome to the GlucoMeter App!")
    return render(request, USER_BASE_TEMPLATE, {})


def register(request):
    form = None
    if request.method == POST_STR:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            logger.debug(f"Creating a new user with username: {username}")
            form.save()
            logger.info(f"User {username} has been successfully created.")
            messages.add_message(request, messages.SUCCESS, "You have successfully registered with GlucoMeter.")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, username, password)
            return redirect('home')
        else:
            form = UserCreationForm(request.POST)
            logger.warning(f"User form error: {form.errors}")

    # For GET queries
    if not form:
        form = UserCreationForm()

    return render(request, USER_REGISTRATION_TEMPLATE, {'form': form})


def user_login(request):
    if request.method == POST_STR:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            logger.debug(f"Logging in user: {username}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.debug("User is valid. Login in successful.")
                messages.add_message(request, messages.SUCCESS, "You have successfully logged in.")
                return redirect('home')
            else:
                logger.warning(f"Invalid user: {username}. Login failed.")

        else:
            logger.warning(f"Form is invalid with errors: {form.errors}")

    # For GET queries
    else:
        form = AuthenticationForm()

    return render(request, USER_LOGIN_TEMPLATE, context={'form': form})


def user_logout(request):
    logger.info(f"Logging out the current user {request.user}")
    logout(request)
    return redirect("login")


@login_required
def update_user(request):
    if request.method == POST_STR:
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            logger.info(f"Updating user: {request.user}")
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your profile has been update successfully.")

    form = UserProfileUpdateForm(instance=request.user)

    return render(request, USER_PROFILE_UPDATE_TEMPLATE, context={'form': form})

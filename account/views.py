from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'home/login.html',{'form': form})


###########################################################################
#                                  user registration                      #
###########################################################################

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.name = new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'home/dashboard.html', {'form': form})  # Redirect to the login page or any other page
        else:
            return render(request, 'account/register.html', {'form': form})  # Return form with errors
    else:
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_done')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def edit_done(request):
    return render(request,'registration/edit_done.html')

@login_required
def dashboad(request):
    return render(request, 'home/dashboard.html', {'section': 'dashboard'})


from django.shortcuts import render,HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

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

@login_required
def dashboad(request):
    return render(request, 'home/dashboard.html', {'section': 'dashboard'})
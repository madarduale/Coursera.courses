

from django.contrib import messages
# from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm
from django.shortcuts import render, redirect
# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            # user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, 'account was created succesfully')
            return redirect('Login')
            # return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})





# def accounts_index(request):
#     form = CreateUserForm()
#     if request == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'account was created succesfully' + user)
#             return redirect('/accounts/Login/')
#     context = {
#         'form':form
#     }
#     return render(request, 'register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('hello_world')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('hello_world')
			else:
				messages.info(request, 'Username OR password is incorrect')
				return redirect('hello_world')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Login')





# def Login(request):
#     return render(request, '/accounts/login.html')
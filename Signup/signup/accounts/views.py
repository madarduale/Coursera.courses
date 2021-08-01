# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_text
# from django.contrib.auth.models import User
# from django.db import IntegrityError
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from .tokens import account_activation_token
# from django.template.loader import render_to_string

# from .forms import SignUpForm
# from .tokens import account_activation_token
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect

def home_view(request):
    return render(request, 'home.html')

# def activation_sent_view(request):
#     return render(request, 'activation_sent.html')


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.signup_confirmation = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'activation_invalid.html')

def signup_view(request):
    
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            # user.profile.first_name = form.cleaned_data.get('first_name')
            # user.profile.last_name = form.cleaned_data.get('last_name')
            # user.profile.email = form.cleaned_data.get('email')
            # user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
            messages.success(request, 'user is created successfully')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
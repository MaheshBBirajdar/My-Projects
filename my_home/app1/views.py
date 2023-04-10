from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def Home(request):
	return render(request,'app1/base.html')


def User_Signup(request):
	form = UserCreationForm()
	context = {'form':form}
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"Register Successfully")
			return redirect('home_page')
		
	return render(request,'app1/register.html', context)


def User_Signin(request):
	form = AuthenticationForm()
	context = {'form':form}
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request,user)
				messages.success(request, f"Login Successfully")
				return redirect('home_page')
			else:
				messages.error(request, f"username & password is incorrect")

	return render(request,'app1/login.html', context)			


def User_Signout(request):
	logout(request)
	return render(request,'app1/logout.html')	



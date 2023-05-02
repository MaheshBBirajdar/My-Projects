from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage



def home(request):
    return render(request,'user/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'user/register.html',context )




def Login(request):
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
				return redirect('homepage')
			else:
				messages.error(request, f"username & password is incorrect")

	return render(request,'user/login.html', context)	



def Logout(request):
	logout(request)
	return render(request,'user/logout.html')	




def EmailSend(request):
    email = EmailMessage(
			'Regarding New Shots Added ',                                        # subject of mail
			'Pl kindly find the new shots from the sheet',                       # body of mail
			'maheshb@osvfx.com',                                                 # from email address
			['all@osvfx.com'],                                                   # list of recipient email addresses
			['riaz@osvfx.com', 'swapnil@osvfx.com','abhishek@osvfx.com'],        # list of CC email addresses (optional)
#			reply_to=['reply-to@example.com'],                                   # list of reply-to email addresses (optional)
			)

    email.send()                                                                 # send the email
    return HttpResponse('Email sent successfully.')                              # return the HTTP response





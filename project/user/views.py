from django.shortcuts import render, redirect
from .forms import SignUp, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from .models import Profile as myprofile
from django.contrib.auth.decorators import login_required


def Register(request):
	form = SignUp()
	context = {'form':form, 'legend': 'Register Yourself'}

	if request.method == 'POST':
		form = SignUp(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f"Account Created")

	return render (request,'user/disform.html',context)


@login_required(login_url='login')
def Profile(request):
	context = {'ip':request.META['REMOTE_ADDR']}
	return render (request, 'user/profile.html', context)



def Profile_user(request, id1):
	u1 = User.objects.filter(id=id1)[0]
	context = {'user1':u1}
	return render (request, 'user/profile_user.html', context)



def Loginpage(request):
	form = AuthenticationForm()
	context = {'form':form, 'legend': 'Login'}

	next=""
	if request.GET:
		next = request.GET['next']

	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			user1 = request.POST.get('username')
			pass1 = request.POST.get('password')
			user = authenticate(request,username=user1, password=pass1)
			if user is not None:
				login(request,user,backend='django.contrib.auth.backends.ModelBackend')
				if next=="" :
					return redirect('profile')
				else:
					return redirect(next)
			else:
				messages.warning(request,"Username and Password is incorrect")


	return render (request, 'user/disform.html', context)



@login_required(login_url='login')
def UpdateProfile1(request):
	try:
		if request.method =='POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request,"Profile Updated")
				return redirect('profile')
		
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		context = {'u_form': u_form, 'p_form': p_form, 'legend': 'Update Your Profile'}
		return render(request,'user/update.html', context)
	
	except ValueError:
		myprofile.objects.create(user=request.user)

	except Exception as e:
		print(e)
		messages.warning(request,'Refresh please')
		myprofile.objects.create(user=request.user)



@login_required(login_url='login')
def user_change_pass(request):

	if request.method=='POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,"Password Changed Successfully")
			return redirect('profile')

	form = PasswordChangeForm(user=request.user)
	context = {'form':form, 'legend': "Change Your Password"}
	return render(request, 'user/disform.html', context)

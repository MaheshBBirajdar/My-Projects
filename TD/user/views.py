from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
import pandas as pd




##############################################################################################

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

##############################################################################################



def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/index.html')




def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/studentclick.html')




def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/adminclick.html')




def adminsignup_view(request):
    form = AdminSigupForm()
    if request.method=='POST':
        form = AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'user/adminsignup.html',{'form':form})




def studentsignup_view(request):
    form1 = StudentSigupForm()
    form2 = StudentExtraForm()
    context = {'form1':form1,'form2':form2}
    if request.method=='POST':
        form1 = StudentSigupForm(request.POST)
        form2 = StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user =  user
            user2 = f2.save()

            my_student_group = Group.objects.get_or_create(name='ARTIST')
            my_student_group[0].user_set.add(user)

        return HttpResponseRedirect('studentlogin')
    return render(request,'user/studentsignup.html',context)
   




def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()




def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'user/adminafterlogin.html')
    else:
        return render(request,'user/studentafterlogin.html')
            



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def allartist_view(request):                                             # All Artist
    artists = StudentExtra.objects.all().order_by("aid")
    context = {'artists':artists}
    return render(request,'user/allartist.html', context)





@login_required(login_url='adminlogin')                                   # Artist Update
@user_passes_test(is_admin)
def editartist_view(request, id):
    object = get_object_or_404(StudentExtra, id=id)
    if request.method == "POST":
        form = StudentExtraForm(request.POST, instance=object)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return render(request,'user/artistupdated.html')
    else:
        form = StudentExtraForm(instance=object)
    context = {'form':form,'object': object,}
    return render(request,'user/editartist.html',context)






@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def deleteartist_view(request,pk):                                       # Delete Artist
    obj = get_object_or_404(StudentExtra, pk=pk)
    obj.delete()
    return render(request,'user/deleteartist.html')






@login_required(login_url='adminlogin')                                  # Import Excel Data
@user_passes_test(is_admin)
def import_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file,engine='openpyxl')
        for index, row in df.iterrows():
            obj = Shot2.objects.create( project_name     = row['field1'],
                                        shot_name        = row['field2'],
                                        work_description = row['field1'],
                                        date_started     = row['field1'],
                                        work_status      = row['field1'],
                                        eta              = row['field1'],
                                        )
            obj.save()
    return render(request, 'user/importdata.html')





@login_required(login_url='adminlogin')                                   # Create/Post
@user_passes_test(is_admin)
def addshot_view(request):
    form=ShotForm()
    if request.method=='POST':
        form=ShotForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'user/shotadded.html')
    context = {'form':form}
    return render(request,'user/addshot.html',context)




 
@login_required(login_url='adminlogin')                                   # Read Shot
def allshot_view(request,page=1):
    shots = Shot2.objects.all().order_by("-date_started")
    p1 = Paginator(shots,20)
    shot = p1.page(page)
    context = {'shots':shot}
    return render(request,'user/allshot.html',context)




@login_required(login_url='adminlogin')                                   # Update Shot
@user_passes_test(is_admin)
def editshot_view(request, id):
    object = get_object_or_404(Shot2, id=id)
    if request.method == "POST":
        form = EditShotForm(request.POST, instance=object)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return render(request,'user/shotupdated.html')
    else:
        form = EditShotForm(instance=object)
    context = {'form':form,'object': object,}
    return render(request,'user/editshot.html',context)




@login_required(login_url='adminlogin')                                   # Delete Shot
@user_passes_test(is_admin)
def deleteshot_view(request, pk):
    shot_obj = get_object_or_404(Shot2, pk=pk)
    shot_obj.delete()
    return render(request,'user/deleteshot.html')



def searchshot_view(request):                                            # Search Shot
    if request.method == 'GET':
        query1 = request.GET.get('p')
        query2 = request.GET.get('q')
        
        if query1 :
            shots = Shot2.objects.filter(project_name__icontains=query1) 
            return render(request, 'user/search.html', {'shots':shots})
        
        elif query2 :
            shots = Shot2.objects.filter(shot_name__icontains=query2) 
            return render(request, 'user/search.html', {'shots':shots})
        
        else:
            print("No Information Available")
    else:
        return render(request,'user/search.html')
         



@login_required(login_url='adminlogin')                                  # Issue Shot
@user_passes_test(is_admin)
def issueshot_view(request):
    form = IssuedShotForm()
    context = {'form':form}
    if request.method == 'POST':
        form = IssuedShotForm(request.POST)
        if form.is_valid():
            obj = IssuedShot()
            obj.department=request.POST.get('department1')
            obj.shot_name=request.POST.get('projectname1')
            obj.project_name = request.POST.get('shotname1')
            obj.save()
            return render(request,'user/shotissued.html')
    return render(request,'user/issueshot.html',context)



####################################################################################################################################

@login_required(login_url='adminlogin')                                    # View Issued Shot
@user_passes_test(is_admin)
def viewissuedshot_view(request):
    issuedshots = IssuedShot.objects.all().order_by("-id")
    li=[]
    j=0
    for i in issuedshots:
        issdate = str(i.issuedate.day)+'-'+str(i.issuedate.month)+'-'+str(i.issuedate.year)
        artists = StudentExtra.objects.filter(department = i.department)
        t=(artists[0].get_name, 
           artists[0].department, 
           artists[0].designation, 
           issuedshots[j].shot_name, 
           issuedshots[j].project_name, 
           issdate,
           i.id)
        j+=1
        li.append(t)

    context = {'li':li}
    return render(request,'user/viewissuedshot.html', context)




@login_required(login_url='adminlogin')                                      # Delete Issued shot
@user_passes_test(is_admin)
def deleteissuedshot_view(request, pk):
    shot_obj = get_object_or_404(IssuedShot, pk=pk)
    shot_obj.delete()
    return render(request,'user/deleteissuedshot.html')


#################################################################################################################################33



@login_required(login_url='studentlogin')                                    # Shot Issued By Artist
def viewissuedshotbyartist_view(request):
    artist = StudentExtra.objects.filter(user_id = request.user.id)
    issuedshot = IssuedShot.objects.filter(department = artist[0].department).order_by('-id')
    li1=[]
    for i in issuedshot:
        issdate = str(i.issuedate.day)+'-'+str(i.issuedate.month)+'-'+str(i.issuedate.year)
        t=(request.user, 
           artist[0].department, 
           artist[0].designation, 
           i.shot_name, 
           i.project_name, 
           issdate)
        li1.append(t)

    context = {'li1':li1}
    return render(request,'user/viewissuedshotbyartist.html', context)





@login_required(login_url='studentlogin')                                      # Send  Feedback     
def sendfeedback_view(request):
    form = SendFeedbackForm()
    if request.method=='POST':
        form = SendFeedbackForm(request.POST)
        if form.is_valid():
            d1 = form.save(commit=False)
            d1.sender = request.user
            form.save()
            return render(request,'user/feedbackadded.html')
        
    context = {'form':form}
    return render(request,'user/addfeedback.html',context)





@login_required(login_url='adminlogin')                                       # Read Feedback
@user_passes_test(is_admin)                                         
def allfeedback_view(request):
    feedbacks = SendFeedback.objects.all().order_by('department', '-date_posted')
    feedbacks_by_department = {}

    for feedback in feedbacks:
        department = feedback.department
        if department in feedbacks_by_department:
            feedbacks_by_department[department].append(feedback)
        else:
            feedbacks_by_department[department] = [feedback]
    context = {'feedbacks_by_department': feedbacks_by_department}
    return render(request, 'user/allfeedback.html', context)





@login_required(login_url='adminlogin')                                       # Delete Feedback
def deletefeedback_view(request, pk):
    shot_obj = get_object_or_404(SendFeedback, pk=pk)
    shot_obj.delete()
    return render(request,'user/deletefeedback.html')





@login_required(login_url='studentlogin')                                      # My Feedback
def myfeedback_view(request):
    current_user = request.user
    feedback = SendFeedback.objects.filter(sender=current_user)
    context = {'feedbacks':feedback}
    return render(request,'user/myfeedback.html',context)



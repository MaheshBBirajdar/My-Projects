from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
import pandas as pd
from django.db.models import F
from datetime import date
from django.db.models import Count
from datetime import datetime


###########################################################################################################################################

def home(request):
    return render(request,'user/home.html')

###########################################################################################################################################

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

###########################################################################################################################################

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

############################################################################################################################################

def Logout(request):
	logout(request)
	return render(request,'user/logout.html')	

############################################################################################################################################

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/index.html')

#############################################################################################################################################

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/studentclick.html')

#############################################################################################################################################

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/adminclick.html')

#############################################################################################################################################

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

##############################################################################################################################################

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
   
################################################################################################################################################

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

#################################################################################################################################################

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'user/adminafterlogin.html')
    else:
        return render(request,'user/studentafterlogin.html')
            
##################################################################################################################################################

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def allartist_view(request):                                                                      # All Artist
    artists = StudentExtra.objects.all().order_by("aid")
    context = {'artists':artists}
    return render(request,'user/allartist.html', context)

##################################################################################################################################################

@login_required(login_url='adminlogin')                                                          # Edit/Update Artist 
@user_passes_test(is_admin)
def editartist_view(request, id):
    object = get_object_or_404(StudentExtra, id=id)
    if request.method == "POST":
        form = StudentExtraForm(request.POST, instance=object)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Artist details updated successfully!')
            return redirect('allartist1')
    else:
        form = StudentExtraForm(instance=object)
    context = {'form':form,'object': object,}
    return render(request,'user/editartist.html',context)

##################################################################################################################################################

@login_required(login_url='adminlogin')
@user_passes_test(is_admin) 
def deleteartist_view(request,pk):                                                                # Delete Artist
    obj = get_object_or_404(StudentExtra, pk=pk)
    obj.delete()
    messages.success(request, 'Artist removed successfully!')
    return redirect('allartist1')

##################################################################################################################################################

@login_required(login_url='adminlogin')                                                           # Import Excel Data
@user_passes_test(is_admin)
def import_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        file_extension = excel_file.name.split('.')[-1].lower()
        
        if file_extension == 'xlsx':
            engine = 'openpyxl'

        elif file_extension == 'xls':
            engine = 'xlrd'

        else:
            return render(request, 'user/importdata.html', {'message': 'Invalid file format. Only (.xlsx) and (.xls) files are supported.'})

        df = pd.read_excel(excel_file, engine=engine)
        df.fillna('N/A', inplace=True) 
        
        imported_rows = 0
        error_rows = 0

        for index, row in df.iterrows():
            project_name = row['Project Name']
            shot_name    = row['Shot Name']

            existing_shot1 = Shot2.objects.filter(project_name=project_name, shot_name=shot_name).first()
            if existing_shot1:
                existing_shot1.date_started     = row['Date Posted']
                existing_shot1.work_description = row['Scope of Work']
                existing_shot1.eta              = row['TGT Date']
#                existing_shot1.work_status      = row['Shot Status']
                existing_shot1.save()

            existing_shot = Shot2.objects.filter(project_name=project_name, shot_name=shot_name).exists()
            if not existing_shot:
                date_started = row['Date Posted']
                eta = row['TGT Date']
                if date_started < eta:
                    obj = Shot2.objects.create(
                        project_name     = project_name,
                        shot_name        = shot_name,
                        work_description = row['Scope of Work'],
                        date_started     = date_started,
                        eta              = eta,
                        work_status      = row['Shot Status']
                    )
                    obj.save()
                    imported_rows += 1
                else:
                    error_rows += 1

        if imported_rows > 0:
            message = f"New {imported_rows} shots added successfully."
            
        else:
            message = "Some changes done."

        if error_rows > 0:
            message += f" {error_rows} rows skipped due to invalid dates."

        return render(request, 'user/importdata.html', {'message': message})
    else:
        return render(request, 'user/importdata.html')

###########################################################################################################################################

@login_required(login_url='adminlogin')                                                     # Create/Add Shot
@user_passes_test(is_admin)
def addshot_view(request):
    form=ShotForm()
    if request.method=='POST':
        form=ShotForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Shot added successfully!')
            return redirect('allproject')
    context = {'form':form}
    return render(request,'user/addshot.html',context)

#############################################################################################################################################

@login_required(login_url='adminlogin')                                                     # Read/All Shot
def allshot_view(request):
    shots = Shot2.objects.all().order_by('project_name')
    paginator = Paginator(shots, 20)
    page = request.GET.get('page')
    shots = paginator.get_page(page)
    context = {'shots': shots}
    return render(request, 'user/allshot.html', context)



@login_required(login_url='adminlogin')                                                     # Read/All Shot for management
def allshot_view1(request, page=1):
    shots = Shot2.objects.all().order_by('project_name')
    paginator = Paginator(shots, 20)
    page = request.GET.get('page')
    shots = paginator.get_page(page)
    context = {'shots': shots}
    return render(request, 'user/mang_message1.html', context)


@login_required(login_url='adminlogin')                                                       # Reviewed Shot
def reviewed_shot(request, shot_id):
    shot = Shot2.objects.get(pk=shot_id)
    shot.work_status = 'REVIEWED'
    shot.save()
    messages.success(request, 'Shot Reviewed')
    return redirect('allshot')


@login_required(login_url='adminlogin')                                                       # Final Approved Shot
def final_approved_shot(request, shot_id):
    shot = Shot2.objects.get(pk=shot_id)
    shot.final_status = 'APPROVED'
    shot.save()
    messages.success(request, 'Shot Approved')
    return redirect('mang_message1')

#############################################################################################################################################

@login_required(login_url='adminlogin')                                                     # Read/All Project
def allproject_view(request):
    projects = Shot2.objects.values('project_name').annotate(num_shots=Count('project_name')).order_by('project_name')
    context = {'projects': projects}
    return render(request, 'user/allproject.html', context)

#############################################################################################################################################

@login_required(login_url='adminlogin')                                                     # All shot by selected project
def project_shots_view(request, project_name):
    shots = Shot2.objects.filter(project_name=project_name)
    today = date.today()

    for shot in shots:
        if shot.work_status != 'READY FOR REVIEW' and shot.eta < today :
            shot.overdue_days = (today - shot.eta).days

        elif shot.work_status == 'READY FOR REVIEW' :
            shot.overdue_days = '-'

        else:
            shot.overdue_days = 0

    context = {'project_name': project_name, 'shots': shots}
    return render(request, 'user/pshots.html', context)

#############################################################################################################################################

@login_required(login_url='adminlogin')                                                     # Update/Edit Shot
@user_passes_test(is_admin) 
def editshot_view(request, id):
    object = get_object_or_404(Shot2, id=id)
    if request.method == "POST":
        form = EditShotForm(request.POST, instance=object)
        if form.is_valid():
            data = form.save(commit=False)
            data.dependency.set(form.cleaned_data['dependency'])
            data.save()
            messages.success(request, 'Shot updated successfully!')
            return redirect('allshot')
    else:
        form = EditShotForm(instance=object)
    context = {'form':form,'object': object,}
    return render(request,'user/editshot.html',context)

#############################################################################################################################################

@login_required(login_url='adminlogin')                                                     # Delete Shot
@user_passes_test(is_admin)
def deleteshot_view(request, pk):
    shot_obj = get_object_or_404(Shot2, pk=pk)
    shot_obj.delete()
    messages.success(request, 'Shot removed successfully!')
    return redirect('allshot')

#############################################################################################################################################

def searchshot_view(request):                                                                 # Search All Shot
    if request.method == 'GET':
        query1 = request.GET.get('p')
        query2 = request.GET.get('q')
        query3 = request.GET.get('r')
        query4 = request.GET.get('s')

        if query1:
            shots = Shot2.objects.filter(project_name__istartswith=query1)
            return render(request, 'user/search.html', {'shots': shots})

        elif query2:
            shots = Shot2.objects.filter(shot_name__istartswith=query2) 
            return render(request, 'user/search.html', {'shots': shots}) 

        elif query3:
            shots = Shot2.objects.filter(work_status__istartswith=query3)
            return render(request, 'user/search.html', {'shots': shots})
        
        elif query4:
            date = datetime.strptime(query4, '%d/%m/%Y').date()  
            shots = Shot2.objects.filter(eta=date)
            return render(request, 'user/search.html', {'shots': shots})

    else:
        return render(request, 'user/search.html')   

############################################################################################################################################

def searchprojectshot_view(request):                                              # Search Shot Project Wise
    if request.method == 'GET':
        query1 = request.GET.get('p1')

        if query1:
            shots = Shot2.objects.filter(shot_name__istartswith=query1) 
            today = date.today()
            for shot in shots:
                if shot.eta and shot.work_status != 'DONE':
                    if today > shot.eta:
                        overdue_days = (today - shot.eta).days
                        shot.overdue_days = overdue_days
                    else:
                        shot.overdue_days = 0
            return render(request, 'user/search1.html', {'shots': shots})
        
        else:
            print("No Information Available")
    else:
        return render(request, 'user/search1.html') 

############################################################################################################################################

def search_issuedshots_view(request):                                           # Search Issued Shot
    dept_name = request.GET.get('p2')
    project_name = request.GET.get('p3')
    shot_name = request.GET.get('p4')
    work_status = request.GET.get('p5')

    issuedshots = IssuedShot.objects.all().order_by("-eta")

    if dept_name:
        issuedshots = issuedshots.filter(department=dept_name)

    if project_name:
        issuedshots = issuedshots.filter(project_name=project_name)

    if shot_name:
        issuedshots = issuedshots.filter(shot_name=shot_name)

    if work_status:
         issuedshots = issuedshots.filter(work_status=work_status)

    def is_all_done(shot_name):
        return IssuedShot.objects.filter(shot_name=shot_name).exclude(work_status='DONE').count() == 0

    for issuedshot in issuedshots:
        if not hasattr(issuedshot, 'work_status') or issuedshot.work_status is None:
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='YTS')

        elif is_all_done(issuedshot.shot_name):
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='Ready for Review')

        else:
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='Pending for Review')

    li = []
    today = date.today()
    for issuedshot in issuedshots:
        eta = issuedshot.eta
        overdue_days = (today - eta).days if issuedshot.work_status != 'DONE' and eta < today else 0
        issdate = issuedshot.issuedate.strftime('%d/%m/%Y')
        artists = StudentExtra.objects.filter(department=issuedshot.department)
        t = (artists[0].get_name,
             issuedshot.project_name,
             issuedshot.shot_name,
             artists[0].department,
             artists[0].designation,
             issdate,
             issuedshot.eta,
             issuedshot.work_status,
             overdue_days,
             issuedshot.id
             )
        li.append(t)

    context = {'li': li}
    return render(request, 'user/search2.html', context)

##############################################################################################################################################

def searchshot_mang_view(request):                                                                 # Search All Shot for Management
    if request.method == 'GET':
        query1 = request.GET.get('p')
        query2 = request.GET.get('q')
        query3 = request.GET.get('r')

        if query1:
            shots = Shot2.objects.filter(project_name__istartswith=query1)
            return render(request, 'user/search3.html', {'shots': shots})

        elif query2:
            shots = Shot2.objects.filter(shot_name__istartswith=query2) 
            return render(request, 'user/search3.html', {'shots': shots}) 

        elif query3:
            shots = Shot2.objects.filter(work_status__istartswith=query3)
            return render(request, 'user/search3.html', {'shots': shots})
        
    else:
        return render(request, 'user/search3.html')   

        
############################################################################################################################################

@login_required(login_url='adminlogin')                                                      # Assign Shot
@user_passes_test(is_admin)
def issueshot_view(request):
    form = IssuedShotForm()
    context = {'form':form}
    if request.method == 'POST':
        form = IssuedShotForm(request.POST)
        if form.is_valid():
            obj = IssuedShot()
            obj.department = request.POST.get('department1')
            obj.shot_name = request.POST.get('shotname1')
            obj.project_name = request.POST.get('projectname1')
            obj.eta = request.POST.get('eta1')
            obj.note = request.POST.get('note1')
            obj.work_status = 'YTS' 

            obj.save()
            messages.success(request, 'Shot assigned successfully!')
            return redirect('viewissuedshot')
    else:
        shot_name = request.GET.get('shot_name')
        project_name = request.GET.get('project_name')
        if shot_name and project_name:
            form.initial['shotname1'] = shot_name
            form.initial['projectname1'] = project_name
    context['form'] = form
    return render(request,'user/issueshot.html',context)

#################################################################################################################################################

@login_required(login_url='adminlogin')                                                      # Re-Assign Shot
@user_passes_test(is_admin)
def re_issueshot_view(request):
    form = IssuedShotForm()
    context = {'form':form}
    if request.method == 'POST':
        form = IssuedShotForm(request.POST)
        if form.is_valid():
            obj = IssuedShot()
            obj.department = request.POST.get('department1')
            obj.shot_name = request.POST.get('shotname1')
            obj.project_name = request.POST.get('projectname1')
            obj.eta = request.POST.get('eta1')
            obj.note = request.POST.get('note1')
            obj.work_status = 'YTS' 

            obj.save()
            messages.success(request, 'Shot assigned successfully!')
            return redirect('viewissuedshot')
    else:
        shot_name = request.GET.get('shot_name')
        project_name = request.GET.get('project_name')
        if shot_name and project_name:
            form.initial['shotname1'] = shot_name
            form.initial['projectname1'] = project_name
    context['form'] = form
    return render(request,'user/reissueshot.html',context)

############################################################################################################################################

@login_required(login_url='adminlogin')                                                                          # View Issued Shot
@user_passes_test(is_admin)
def viewissuedshot_view(request):
    issuedshots = IssuedShot.objects.all().order_by("-eta")

    def is_all_done(shot_name):
        return IssuedShot.objects.filter(shot_name=shot_name).exclude(work_status='DONE').count() == 0

            
    for issuedshot in issuedshots:
        if not hasattr(issuedshot, 'work_status') or issuedshot.work_status is None:
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='YTS')

        elif is_all_done(issuedshot.shot_name):
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='READY FOR REVIEW')
            issuedshot.delete()

        else:
            Shot2.objects.filter(shot_name=issuedshot.shot_name).update(work_status='PENDING FOR REVIEW')

    li = []
    today = date.today()
    
    for issuedshot in issuedshots:
        eta = issuedshot.eta
#        overdue_days = (today - eta).days if issuedshot.work_status != 'DONE' and eta < today else 0

        if issuedshot.work_status != 'DONE' and eta < today:
            overdue_days = (today - eta).days
    
        elif issuedshot.work_status == 'DONE' :
            overdue_days = '-'
            
        else :
            overdue_days = 0

        issdate = issuedshot.issuedate.strftime('%d/%m/%Y')
        artists = StudentExtra.objects.filter(department=issuedshot.department)
        t = (artists[0].get_name,
             issuedshot.project_name,
             issuedshot.shot_name,
             artists[0].department,
             artists[0].designation,
             issdate,
             issuedshot.eta,
             issuedshot.work_status,
             overdue_days,
#             issuedshot.id,
             )
        li.append(t)
    context = {'li': li}
    return render(request, 'user/viewissuedshot.html', context)

############################################################################################################################################

@login_required(login_url='adminlogin')                                                        # Delete Issued shot
@user_passes_test(is_admin)
def deleteissuedshot_view(request, pk):
    shot_obj = get_object_or_404(IssuedShot, pk=pk)
    shot_obj.delete()
    messages.success(request, 'Assigned shot removed successfully!')
    return redirect('viewissuedshot')

#############################################################################################################################################

@login_required(login_url='studentlogin')                                                      # Shot Issued By Artist
def viewissuedshotbyartist_view(request):
    artist = StudentExtra.objects.filter(user_id = request.user.id)
    issuedshots = IssuedShot.objects.filter(department = artist[0].department).order_by('-id')
    li1=[]
    for issuedshot in issuedshots:
#        issdate = str(issuedshot.issuedate.day)+'-'+str(issuedshot.issuedate.month)+'-'+str(issuedshot.issuedate.year)
        issdate = issuedshot.issuedate.strftime('%d/%m/%Y')
        t=(request.user.first_name, 
           artist[0].department, 
           artist[0].designation, 
           issuedshot.project_name, 
           issuedshot.shot_name, 
           issdate,
           issuedshot.eta,
           issuedshot.note,
           issuedshot.work_status,)
        li1.append(t)

    context = {'li1':li1}
    return render(request,'user/viewissuedshotbyartist.html', context)

##############################################################################################################################################

@login_required(login_url='studentlogin')                                                       # Send  Shot Status     
def sendfeedback_view(request):
    form = SendFeedbackForm()
    if request.method == 'POST':
        form = SendFeedbackForm(request.POST)
        if form.is_valid():
            d1 = form.save(commit=False)
            d1.sender1 = request.user

            project_name = form.cleaned_data['project_name']
            shot_name = form.cleaned_data['shot_name']
            issued_shots = IssuedShot.objects.filter(project_name=project_name, shot_name=shot_name)

            if issued_shots.exists():
                authorized_shot = None
                for issued_shot in issued_shots:
                    if issued_shot.department == d1.department:
                        authorized_shot = issued_shot
                        break

                if authorized_shot:
                    if authorized_shot.work_status == 'DONE':
                        messages.error(request, 'Work status has already been sent to DONE for this shot.')
                    else:
                        d1.work_status = form.cleaned_data['work_status']
                        authorized_shot.work_status = d1.work_status
                        authorized_shot.save()
                        d1.issued_shot = authorized_shot
                        d1.save()
                        messages.success(request, 'Shot status sent successfully!')
                else:
                    form.add_error(None, 'You are not authorized to send shot status for this shot.')
                    messages.error(request, 'You are not authorized to send shot status for this shot.')
            else:
                form.add_error('shot_name', 'IssuedShot Not found with the given project and shot names.')
    context = {'form': form}
    return render(request, 'user/addfeedback.html', context)


#################################################################################################################################################

@login_required(login_url='adminlogin')                                                         # Read Shot Status
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

#################################################################################################################################################

@login_required(login_url='studentlogin')                                                       # My Shot Status
def myfeedback_view(request):
    current_user = request.user
    feedback = SendFeedback.objects.filter(sender1=current_user).order_by('-date_posted')
    context = {'feedbacks':feedback}
    return render(request,'user/myfeedback.html',context)

####################################################################################################################################################

@login_required(login_url='adminlogin')                                                         # Delete Shot Status
def deletefeedback_view(request, pk):
    shot_obj = get_object_or_404(SendFeedback, pk=pk)
    shot_obj.delete()
    messages.success(request, 'Shot status removed successfully!')
    return redirect('allfeedback')

#################################################################################################################################################

@login_required(login_url='studentlogin') 
def artist_portal(request):                                                                     # receive popup message when shot added
    messages = ArtistMessage.objects.order_by('-date_sent')
    context = {'messages': messages}
    return render(request, 'user/message.html', context)

###################################################################################################################################################

@login_required(login_url='adminlogin') 
def management_portal(request):                                                                 # receive popup message when shot status updated to Reviewed
    messages1 = ManagementMessage.objects.order_by('-date_sent')
    shots = Shot2.objects.all().order_by('project_name')
    message_count = ManagementMessage.objects.aggregate(count=Count('id'))['count']
    context = {'messages1': messages1,'message_count':message_count, 'shots':shots}
    return render(request, 'user/mang_message.html', context)

###################################################################################################################################################

@login_required(login_url='adminlogin')                                                         # Delete mang_messages                                            
@user_passes_test(is_admin)
def delete_mang_message_view(request, pk):
    shot_obj = get_object_or_404(ManagementMessage, pk=pk)
    shot_obj.delete()
    messages.success(request, 'Removed')
    return redirect('popup_mang_message')  




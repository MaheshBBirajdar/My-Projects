from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import pandas as pd
from django.db.models import Q
from .forms import SearchForm


#################################################################################

# export LD_LIBRARY_PATH=/usr/local/lib

#################################################################################

def Upload_csv1(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file, engine='openpyxl',)
        for index, row in df.iterrows():
            Shot1.objects.create(
                                project_name=row[2],
                                shot_number=row[3],
                                task_assign=row[4],
                                work_description=row[5],
                                date_started=row[6],
                                work_status=row[7]
                                )
            return render (request, 'blog/upload_csv2.html', {'message': 'Import successful.'})
    else:
        return render (request, 'blog/upload_csv2.html')


'''
def Upload_csv1(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid(): 
           file = request.FILES['file']
           df = pd.read_excel(file,engine='openpyxl')
           for index, row in df.iterrows():
                Shot1.objects.create(
                                     supervisor=row[1],
                                     project_name=row[2],
                                     shot_number=row[3],
                                     task_assign=row[4],
                                     work_description=row[5],
                                     date_started=row[6],
                                     work_status=row[7]
                                     )
        messages.success(request, 'File uploaded successfully.')
        return redirect('all_shot1')
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'blog/upload_csv1.html', context)
'''

##########################################################################

def Add_Artist1(request):
    if request.method == 'POST':
        form = ArtistForm1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f" New Artist has been added ")
            return redirect('all_artist1')
    else:
        form = ArtistForm1()
    context = {'form':form}
    return render(request,'blog/add_artist1.html',context)

##############################################################################

@login_required
def All_Artist1(request):
    artists = User.objects.all().order_by('-id')
    context = {'artists':artists}
    return render(request,'blog/all_artist1.html',context)


#################################################################################

@login_required
def Add_Shot1(request):
    user = request.user
    if request.method == 'POST':
        form = ShotForm1(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.supervisor = user
            data.save()
            messages.success(request,f" New Task added ")
            return redirect('all_shot1')
    else:
        form = ShotForm1()
    context = {'form':form}
    return render(request,'blog/add_shot1.html',context)

###################################################################################

@login_required
def All_Shot1(request,page=1):
    shots = Shot1.objects.all().order_by("-date_started")
    p1 = Paginator(shots,10)
    shot = p1.page(page)
    context = {'shots':shot,}
    return render(request,'blog/all_shot1.html',context)

######################################################################################

@login_required
def My_Shot1(request):
    current_user = request.user
    shots = Shot1.objects.filter(supervisor=current_user)
    context = {'myshots':shots}
    return render(request,'blog/my_shot1.html',context)

#######################################################################################

@login_required
def Edit_Shot1(request, id):
    object = get_object_or_404(Shot1, id=id)
    if request.user == object.supervisor:
        if request.method == "POST":
            form = ShotFormB(request.POST, instance=object)
            if form.is_valid():
                data = form.save(commit=False)
                data.save()
                messages.success(request,f"Changes done successfully")
                return redirect('all_shot1')
        else:
            form = ShotFormB(instance=object)
    else:
        form = ShotFormB(instance=object)
    context = {'form':form,'object': object,}
    return render(request,'blog/edit_shot1.html',context)

#########################################################################################

@login_required
def Delete_Shot1(request, pk):
    shot_obj = get_object_or_404(Shot1, pk=pk)
    shot_obj.delete()
    messages.success(request,f"Task Deleted Successfully")
    return redirect('my_shot1')

#############################################################################################

@login_required
def IssueShot1(request):
    form=IssuedShotForm1()
    context = {'form':form}
    if request.method=='POST':
        form=IssuedShotForm1(request.POST)
        if form.is_valid():
            obj=IssuedShot1() 
            obj.projectname = request.POST.get('projectname')
            obj.save()
            messages.success(request,f"Shot Issued successfully")
            return redirect('viewissuedshot1')
    return render(request,'blog/issueshot1.html',context)

#############################################################################################

@login_required
def ViewIssuedShot1(request):
    Issuedshots = IssuedShot1.objects.all()
    context = {'Issuedshots':Issuedshots}
    return render(request,'blog/viewissuedshot1.html',context)

##############################################################################################

@login_required
def Delete_Issued_Shot1(request, pk):
    shot_obj = get_object_or_404(IssuedShot1, pk=pk)
    shot_obj.delete()
    messages.success(request,f"Task Deleted Successfully")
    return redirect('viewissuedshot1')

################################################################################################


def Search(request):
    if request.method == "GET":
        query1 = request.GET.get('q')
        query2 = request.GET.get('p')
        query3 = request.GET.get('r')

        if query1:
            shots = Shot.objects.filter(project_name__icontains=query1)  
            return render(request, 'blog/search.html', {'shots':shots})
       
        elif query2:
            shots = Shot1.objects.filter(shot_number__icontains=query2) 
            return render(request, 'blog/search.html', {'shots':shots})
        
        elif query3:
            shots = Shot1.objects.filter(work_status__icontains=query3) 
            return render(request, 'blog/search.html', {'shots':shots})
        
        else:
            print("No Information Available")
            return render(request, 'blog/search.html')
        
    else:
        return render(request, 'blog/search.html')

# shots = Shot.objects.filter(Q(project_name__icontains=query) | Q(work_status__icontains=query) | Q(shot_number__icontains=query))

##################################################################################################









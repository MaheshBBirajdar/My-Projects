from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import pandas as pd
from django.http import HttpResponse

#################################################################################
'''
1.  (su -)
2.  sys66$OS
3.  cd /oshome/maheshb/Pipeline_VFX/openslate
4.  cd sqlite-autoconf-3280000/
5.  export LD_LIBRARY_PATH=/usr/local/lib
6.  kill server - sudo fuser -k 8000/tcp 
'''
#################################################################################

''' 
def Upload_csv1(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file, engine='openpyxl',)
        for index, row in df.iterrows():
            Shot1.objects.create(
                                project_name=row[2],python 
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


def Import_Excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file, engine='openpyxl')
            employees = []
            for _, row in df.iterrows():
                employee = Shot1(
                    shot_number=row[0],
                    project_name=row[1],
                    task_assign=row[2],
                    work_description=row[3],
                    date_started=row[4], 
                    work_status=row[5]
                )
                employees.append(employee)
            Shot1.objects.bulk_create(employees)
            return HttpResponse('Data imported successfully!')
    else:
        form = UploadFileForm()
    return render(request, 'blog/upload_csv2.html', {'form': form})


#############################################################################

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

def AddArtist(request):
	if request.method == 'POST':
		form = ArtistForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'New Artist Added Successfully')
			return redirect('allartist')
	else:
		form = ArtistForm()
	context = {'form':form}
	return render(request, 'blog/add.html',context )

###########################################################################################

def AllArtist(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'blog/all.html', context)

##########################################################################################

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

def Search(request):
    if request.method == "GET":
        query1 = request.GET.get('p')
        query2 = request.GET.get('q')
        query3 = request.GET.get('r')

        if query1:
            shots = Shot1.objects.filter(project_name__icontains=query1)  
            return render(request, 'blog/search.html', {'shots':shots})
       
        elif query2:
            shots = Shot1.objects.filter(shot_name__icontains=query2) 
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









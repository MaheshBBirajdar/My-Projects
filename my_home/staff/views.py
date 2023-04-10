from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages


def Staff_Create(request):
	form = Staff_Form()
	context = {'form':form}
	if request.method =='POST':
		form = Staff_Form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f"Data Created")
			return redirect('view_all')
	return render(request, 'staff/create.html',context)


def Staff_Read(request):
	emp_list = Staff.objects.all()
	context = {'data':emp_list}
	return render(request, 'staff/read.html',context)



def Staff_Update(request,id):
	emp = get_object_or_404(Staff, pk=id)
	form = Staff_Form(instance=emp)
	context = {'data':emp, 'form':form}
	if request.method =='POST':
		form = Staff_Form(request.POST, instance=emp)
		if form.is_valid():
			form.save()
			messages.success(request,f"Data Updated")
			return redirect('view_all')
	
	return render(request, 'staff/edit.html',context)



def Staff_Delete(request,id):
	emp = get_object_or_404(Staff, pk=id)
	context = {'data':emp}
	if request.method =='POST':
		emp.delete()
		return redirect('view_all')
	
	return render(request, 'staff/delete.html',context)



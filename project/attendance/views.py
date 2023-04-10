from django.shortcuts import render
from .forms import StudentForm, StudentMarkForm, StudentMarkFormDisplay
from django.contrib import messages
import time
from .models import Mark_attendance2
# Create your views here.

def StudentMasterForm(request):
	form = StudentForm()
	context = {'form':form, 'legend': 'Register Today'}

	if request.method=='POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			form.save()
			messages.success(request,f'Record Added')
		else:
			messages.success(request, f'Error in form')


	return render (request,'attendance/disform.html',context)


def e_h(t1):
	t9 =time.localtime(t1)
	return time.strftime("%d-%m-%Y-%H",t9)


def Mark_Student(request):
	form = StudentMarkForm()
	context = {'form':form, 'legend': 'Mark Your Attendance'}
	try:
		if request.method=='POST':
			form = StudentMarkForm(request.POST)
			if form.is_valid():
				mark1 = form.save(commit=False)
				mark1.time1 = int(time.time())
				mark1.date1 = e_h(mark1.time1)
				mark1.ip_address = request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT', 'unknown')
				form.save()
				messages.success(request,f"{mark1.uid}, Your attendance is marked")
			else:
				messages.warning(request, f'Error in form')
	except Exception as e:
		messages.warning(request, f'{e}')

	return render (request,'attendance/disform.html',context)


def display_attendance(request):
	posts = Mark_attendance2.objects.all()
	context = {'data':posts}

	return render (request,'attendance/displayatt.html',context)


def One_attendance(request):
	form =StudentMarkFormDisplay()
	context = {'form':form}
	if request.method =='POST':
		form = StudentMarkFormDisplay(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			u1 = d1.get('uid')
			posts = Mark_attendance2.objects.filter(uid=u1)
			context = {'data':posts}
			return render (request,'attendance/displayatt.html',context)

	return render (request,'attendance/disform.html', context)



##############################  Function Based (Rest API)  ###############################
##########################################################################################


from .serializer import Attserializer
from .models import Studentdata2
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



def Studetails(request,pk):
	try:
		stu = Studentdata2.objects.get(id=pk)                          # data from database
		serializer = Attserializer(stu)                                # serial data
		json_data = JSONRenderer().render(serializer.data)             # convert to json data
		print(json_data)
	except Exception as e:
		print(e)
		json_data = "{'Not get':'NIL'}"
	return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def student_api(request):

	if request.method=='GET':
		json_data = request.body                      # get data from myapp.py(in batch4)
		stream=io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)      #  convert to python data
		id1= python_data.get('id',None)
		if id1 is not None:
			print("id",id1)
			stu = Studentdata2.objects.get(id=id1)
			serializer = Attserializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			print(json_data)
			return HttpResponse(json_data, content_type='application/json')



	if request.method=='POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		serializer = Attserializer(data=python_data)
		if serializer.is_valid():
			serializer.save()
			message = {'msg':'Data Created'}
			return JsonResponse(message,safe=False)

		json_data = JSONRenderer().render(serializer.error)
		return HttpResponse(json_data, content_type='application/json') 



	if request.method=='PUT':
		json_data = request.body                      # get data from myapp.py(in batch4)
		stream=io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)      #  convert to python data
		id1= python_data.get('stuid',None)
		stu = Studentdata2.objects.get(stuid=id1)
		serializer = Attserializer(stu, data=python_data, partial=True)
		if serializer.is_valid():
			serializer.save()
			message = {'msg': 'Data Updated'}
			return JsonResponse(message,safe=False)

		json_data = JSONRenderer().render(serializer.error)
		return HttpResponse(json_data, content_type='application/json')




	if request.method =='DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		id1 = python_data.get('stuid',None)
		stu = Studentdata2.objects.get(stuid=id1)
		stu.delete()
		message = {'msg':'Data Deleted'}
		return JsonResponse(message,safe=False)



#################################  Class Based (Rest API)  ##################################
#############################################################################################

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .permissions import MaheshPermission


class StudentListAPIView(ListAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer
	

class StudentCreateAPIView(CreateAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentRetrieveAPIView(RetrieveAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentUpdateAPIView(UpdateAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentDestroyAPIView(DestroyAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentListCreateAPIView(ListCreateAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer
	#authentication_classes = [BasicAuthentication]
	authentication_classes = [SessionAuthentication]
	#permission_classes = [IsAuthenticated]
	#permission_classes = [IsAdminUser]
	#permission_classes = [IsAuthenticatedOrReadOnly]
	#permission_classes = [DjangoModelPermissions]
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
	permission_classes = [MaheshPermission]                              #custom Permission

class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Studentdata2.objects.all()
	serializer_class = Attserializer



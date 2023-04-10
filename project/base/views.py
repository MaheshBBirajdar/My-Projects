from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, PythonDjangoForm
from .models import Student, PythonDjango

def hello(request):
	#print(request)
	#print(request.META.keys())
	#print(request.META['HTTP_USER_AGENT'])
	return HttpResponse('Hello World !')


def hi(request):
	context = {'name': 'mahesh', 'title':'Django Project'}
	return render (request,'base/second.html', context)


def ok(request):
	posts = [
				{	'title':'Post1',
					'author': 'Mahesh',
					'heading' : 'This is my first post'
				},

				{	'title':'Post2',
					'author': 'Rutu',
					'heading' :'This is my first post'
				}

			]

	context = {'posts':posts}
	return render (request,'base/third.html',context)



def pd(request):
	data = [
				{   'Title':'Python',
					'Author': 'Mahesh',
					'Subject':'P & D'
				},

				{	'Title': 'Django',
					'Author': 'Rutu',
					'Subject': 'Bcom'
				}

			]

	context = {'datas':data}
	return render (request, 'base/pd.html', context)



def html(request):
	return render (request,'base/first.html')


def holly(request):
	list1 = ['Thor','I-man', 'Hulk', 'captain']
	context = {'hero': list1}
	return render (request,'base/fourth.html',context)

def Student1(request):
	form = StudentForm()
	context ={'form':form, 'legend': 'Add Your Details'}

	if request.method=='POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			u1 = d1.get('uid')
			n1 = d1.get('name')
			m1 = d1.get('mail')
			c1 = d1.get('sclass')
			Student.objects.create(stuid=u1, stuname=n1, stumail=m1, stuclass=c1)


	return render (request,'base/simpleform.html',context)


def PyD(request):
	form = PythonDjangoForm()
	context = {'forms':form, 'legend':'Add Your Details' }

	if request.method =='POST':
		form = PythonDjangoForm(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			r1 = d1.get('rollnum')
			s1 = d1.get('subject')
			m1 = d1.get('marks')
			PythonDjango.objects.create(roll_no=r1, subject_name=s1, marks_got=m1)

	return render(request,'base/pyd.html',context)

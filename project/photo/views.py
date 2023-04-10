from django.shortcuts import render
from .forms import PicForm
from .models import PhotoGal


def multiple_upload(request):
	img = PhotoGal.objects.all()
	form = PicForm()
	if request.method == 'POST':
		form = PicForm(request.POST,request.FILES)
		files = request.FILES.getlist('multipleimg')
		if form.is_valid():
			for f1 in files:
				gallery = PhotoGal(multipleimg=f1)
				gallery.save()

	context = {'form':form, 'galpic': img}

	return render (request,'photo/upload.html', context)



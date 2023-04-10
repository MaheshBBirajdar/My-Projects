from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm1, CommentForm1
from django.contrib.auth.decorators import login_required
from .models import Post, Comment1
from django.core.paginator import Paginator
from .decorators import allowed_user


################################## Function Based View ##################################

@login_required(login_url='login')
@allowed_user(allowed_roles=['read1','write1'])
def Allpost1(request,page=1):
	posts = Post.objects.all()
	p1 = Paginator(posts,3)
	post = p1.page(page)
	context = {'posts':post}

	return render (request,'blog/allpost.html',context)



def Specificpost1(request,id1):
	post=Post.objects.filter(id=id1)[0]
	context = {'post':post}

	return render (request, 'blog/specpost.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['write1'])
def CreatePost1(request):
	form =PostForm1()
	context = {'form':form}
	if request.method=='POST':
		form = PostForm1(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.author = request.user
			form.save()
			return redirect('fun-allpost')

	return render (request,'blog/createpost.html', context)


@login_required(login_url='login')
def CommentPost1(request,id1):
	form = CommentForm1()
	post = Post.objects.filter(id=id1)[0]
	comments = post.comment_post.all()
	context = {'form':form, 'post':post, 'comments':comments}
	if request.method == 'POST':
		form = CommentForm1(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.post = post 
			mark1.author = request.user
			form.save()

	return render (request, 'blog/comment_post_fun.html', context)



def comment_approve(request,id1):
	comment = get_object_or_404(Comment1,id=id1)
	comment.approve()

	return redirect('fun-post-comment', id1=comment.post.id)




################################### Class Based View #################################


from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class PostCreateView1(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'
	#success_url = '/blog/clsview/'

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostListView1(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'blog/allposts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'            # by default object_list in template
	login_url = '/login/'
	paginate_by = 4


class PostDetailView1(LoginRequiredMixin,DetailView):
	model = Post
	template_name = 'blog/specpost.html'
	context_object_name = 'posts'
	login_url = '/login/'


class UserPostListView1(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'blog/allposts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'            
	login_url = '/login/'
	paginate_by = 4

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)


class OtherUserPostListView1(LoginRequiredMixin,ListView):
	model = Post
	template_name = 'blog/allposts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'            
	login_url = '/login/'
	paginate_by = 4

	def get_queryset(self):
		#user = get_object_or_404(User, username=self.kwargs.get('u1'))
		#return Post.objects.filter(author=user)
		return Post.objects.filter(author=self.kwargs.get('u1'))


class PostUpdateView1(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'
	

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostDeleteView1(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/blog/clsview/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False
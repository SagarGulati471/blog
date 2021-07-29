from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView, 
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
 

def home(request):
    context={
        'posts' : Post.objects.all()
    }
    return  render(request,'blog/home.html',context)


class PostListView(ListView):
    model=Post
    template_name="blog/home.html"  #<app>/<model>_<viewtype>.html
    context_object_name='posts' 
    ordering=['-date_posted']   #By default it is oldest to newest (added minus sign to reverse it)
    paginate_by=2


class PostDetailView(DetailView): #Detail view will be looking in default template name=>  #<app>/<model>_<viewtype>.html   i.e  blog/post_detail.html
    model=Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False





def about(request):
        return  render(request,'blog/about.html')

 
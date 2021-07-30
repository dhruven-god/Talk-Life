from django.shortcuts import render,redirect,reverse,resolve_url,get_object_or_404
from django.views.generic.edit import DeleteView
from .models import Post
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView,CreateView
from django.views import View
from .forms import CommentForm, PostForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-id']


class PostDetailView(View):

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))

        context = {
            "post":post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")

        }        
        
        
        return render(request,"blog/post-detail.html",context)



class WriteView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/write.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete.html"
    success_url = '/'




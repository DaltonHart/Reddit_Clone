from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PostForm, CommentForm, Sub_Form
from .models import Sub_Reddit, CustomUser, Post, Comment

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# index subreddits
def sub_reddit_list(request):
    sub_reddits = Sub_Reddit.objects.all()
    return render(request, 'reddit_clone/sub_reddit_list.html', {'sub_reddits':sub_reddits})

#show subreddit
def sub_reddit_detail(request, pk):
    sub_reddit = Sub_Reddit.objects.get(id=pk)
    return render(request, 'reddit_clone/sub_reddit_detail.html',{'sub_reddit':sub_reddit})

#index Posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'reddit_clone/post_list.html', {'posts':posts})

#index Comments
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'reddit_clone/comment_list.html', {'comments':comments})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'reddit_clone/postform.html', {'form': form})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'reddit_clone/commentform.html', {'form': form})

def sub_create(request):
    if request.method == 'POST':
        form = Sub_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('sub_reddit_list')
    else:
        form = Sub_Form()
    return render(request, 'reddit_clone/subform.html', {'form': form})
    
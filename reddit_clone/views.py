from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Sub_Reddit, CustomUser

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
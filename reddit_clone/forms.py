from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post, Comment, Sub_Reddit

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body','sub_reddit')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', 'post', 'parent')

class Sub_Form(forms.ModelForm):

    class Meta:
        model = Sub_Reddit
        fields = ('name', 'description')
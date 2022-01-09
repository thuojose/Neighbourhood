from django import forms
from .models import notifications, Business,BlogPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class notificationsForm(forms.ModelForm):
    class Meta:
        model = notifications
        exclude = ['author', 'neighbourhood', 'post_date']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['username', 'neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']
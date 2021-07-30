from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name","text"]
        labels = {
            "user_name": "Your Name",
            "text": "Your Comment"
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","body","author"]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':"name",'type':'hidden'}),
        }
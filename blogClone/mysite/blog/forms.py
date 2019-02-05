from django import forms
from blog.models import Post,comments


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title'
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = comments
        fields = ('author','text')

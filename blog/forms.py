from django import form
from .models import Post

class PostForm(forms.ModelsForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
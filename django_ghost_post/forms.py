from django import forms
from django_ghost_post.models import BoastRoast

class PostForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ["choices", "user_post"]
from django.forms import ModelForm
from django import forms
from .models import Topics
class NewTopicForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5 , 'placeholder':'write your message here '}
    ))
    class Meta :
        model = Topics
        fields = ['name','message']
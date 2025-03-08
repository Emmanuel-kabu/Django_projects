from django import forms
from .models import Topic, Entry
from django.forms import ModelForm

class TopicForm(forms.ModelForm):
    class meta:
        model = Topic
        fields = ['text']
        label = {'text:' ''}

class NewEntry(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']  
        label = {'text:' ''} 
        widgets = {'text': forms.Textarea(attrs ={'cols' : 80})}    


    

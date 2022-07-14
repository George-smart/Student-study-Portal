from django import forms
from .models import *


class HomeWorkForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'note_title'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'note_description'
        }
    ))

    class Meta:
        model = HomeWorks
        fields = ['title', 'description', 'is_finished']


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'note_title'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'note_description'
        }
    ))

    class Meta:
        model = Notes
        fields = ['title', 'description']


class FeedbackForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'note_title'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'note_description'
        }
    ))

    class Meta:
        model = Feedback
        fields = ['subject', 'description']

        

    
        
class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['dashboard']

    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=300, label="Enter Your Search")       



from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)
    
class CreateNewNote(forms.Form):
    notetitle = forms.CharField(label="notetitle", max_length=100)
    notetext = forms.CharField(label="notetext", max_length=200, required=False)
    #notetext = forms.CharField(label="notetext",widget=forms.Textarea)
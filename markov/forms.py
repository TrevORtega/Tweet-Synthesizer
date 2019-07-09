from django import forms

class HandleForm(forms.Form):
    handle = forms.CharField(label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Twitter Handle: "@__"'}),  max_length=100)
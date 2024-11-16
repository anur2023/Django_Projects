from django import forms
from .models import Members
class Memberform(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['fname','lname','email','passwd','age']
        
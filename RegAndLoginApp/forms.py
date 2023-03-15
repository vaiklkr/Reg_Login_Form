from django import forms
from RegAndLoginApp.models import Reg 

class RegForm(forms.ModelForm):
    
    class Meta:
        #password=forms.forms.CharField(RangeWidget(base_widget=), max_length=, required=False)
         password=forms.CharField(widget=forms.PasswordInput())
         model = Reg
         widget = {'pwd': forms.PasswordInput()}
         fields = ['user','pwd']

class LoginForm(forms.Form):
     user = forms.CharField(max_length=64)
     pwd = forms.CharField(widget=forms.PasswordInput())


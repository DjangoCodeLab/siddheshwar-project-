from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError 



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['first_name','last_name','username','password1','password2']
        

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("username must be at least 5 characters long.")
        return username 
    

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8 :
            raise ValidationError("Passowrd must be at least 8 characters long")
        
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1!=password2:
            raise ValidationError("Passwords do not match")
        
        return cleaned_data
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))



    
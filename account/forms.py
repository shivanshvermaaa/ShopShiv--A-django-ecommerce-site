from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput, EmailInput


# registartion form
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)

        self.fields['email'].required=True

        # email validation
    def clean_email(self):

        # retrieve email data from the form
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists(): #if same email exists in the database
                raise forms.ValidationError("this email is invalid")
            
        if len(email)>= 350:
                raise forms.ValidationError("the email is too long")
            
        return email

            

# login form

class loginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder':'username','id':'login-username'}))
    password=forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'password','id':'login-password'}))


#update form
class updateUserForm(forms.ModelForm):
    password = None
   
    class Meta:
        model=User
        fields=['username','email']
        exclude=['password1','password2']  # excluding password fields
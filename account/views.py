from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm, loginForm,updateUserForm
from django.contrib.sites.shortcuts import get_current_site
from . token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            subject='account verification email'

            # rendering the email template with the required values
            message=render_to_string('account/registration/email-verification.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':user_tokenizer_generate.make_token(user),
            })
            
            user.email_user(subject=subject,message=message)# sending the email
            # email verification
            return redirect('email-verification-sent')
        
    context={'form':form}
        
    return render(request, 'account/registration/register.html',context=context)

def email_verification(request,uidb64,token):
    
    unique_id=force_str(urlsafe_base64_decode(uidb64))
    user=User.objects.get(pk=unique_id)
    

    if user and user_tokenizer_generate.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')


    

def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')

def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')

def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')

def my_login(request):
    form = loginForm()
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    context = {'form': form}
    return render(request, 'account/my-login.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'account/dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect('store')



@login_required(login_url='my-login')
def profile_management(request):
    
    if request.method=='POST':
        user_form= updateUserForm(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')


    user_form=updateUserForm(instance=request.user)
    
    context={'user_form':user_form}

    return render(request, 'account/profile-management.html',context=context)


def delete_account(request):

    
    if request.method == 'POST':
        user= request.user
        logout(request)
        user.delete()
        return redirect('store')
    else:
        return render(request, 'account/delete-account.html')


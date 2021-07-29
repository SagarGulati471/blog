from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required  #To prevent access without logging in, this decorator adds functionality to  
                                                           #existing function
# Create your views here.


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.warning(request,f'Account created successfully for {username} you can login now')
            print('yes')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form}) 


@login_required                       #With this decorator also add default LOGIN_URL in settings.py file
def profile(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.warning(request,f"Your account has been updated successfully")
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,
            'p_form':p_form}

    return render(request,'users/profile.html',context)






 #Types of messages
'''
    message.debug
    message.info
    message.success
    message.warning
    message.error    
'''
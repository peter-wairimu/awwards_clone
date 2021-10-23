from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project
from .decorators import unauthenticated_user
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,ProjectForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'accounts/register.html',context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('auth')
            
        else:
            messages.info(request,'Username or password is inorrect')
            

    context = {}
    return render(request,'accounts/plogin.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def post(request):
    posts = Project.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')
    user = request.user

    return render(request,'login.html',{'posts':posts,'user':user})

@login_required(login_url='login')
def logincup(request):
    return render(request,'project_details.html')


def userPage(request):
    context = {}

    return render(request,'accounts/user.html',context)



def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'accounts/profile.html', context)



def project_upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image= current_user
            image.save()
            return redirect('auth')

        else:
            form = ProjectForm()
        return render(request, 'project_details.htm', {'form': form})














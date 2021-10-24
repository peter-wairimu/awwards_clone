from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project
from .decorators import unauthenticated_user
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,UploadProjectForm
from django.contrib import messages
from django .contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse

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



def home(request):
    peters=Project.objects.all()

    context={"peters":peters}
    return render (request, 'project.html', context)


def detail(request, id):
    projects=Project.objects.get(id=id)
    context={"project":projects}
    return render(request,'project_details.html',context)


def  add_project(request):
    if request.method=="POST":
        form=UploadProjectForm(request.POST or None)
        if form.is_valid():
            data=form.save(commit=False)
            data.save()
            return redirect ("home")
    else:
        form=UploadProjectForm()
    return render(request, "add_project.html",{"form":form})    


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_articles = Project.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})







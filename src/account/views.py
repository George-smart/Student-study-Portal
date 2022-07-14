from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from .form import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dashboard.models import Dashboard, Profile
from django.contrib.auth.forms import UserChangeForm


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signUp.html'  

    success_url = reverse_lazy('login')

def Signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            username = user.username
            return redirect('introductory_page')
            # return render(request, 'dashboard.html', {'username': username})
        else:
            messages.success(request, "Invalid login details! please enter a corrent username")
            return redirect('login')
    else:
        return render(request, 'registration/signin.html')

def Signout(request):
    logout(request)
    # messages.success(request, "Logout")
    return redirect('login')

class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class ProfileCreation(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'registration/update_profile.html'
    fields = ['profile_pix', 'phone', 'address', 'school', 'faculty', 'department', 'level']

    success_url = reverse_lazy('dashboard')


# def UpdateUserView(request):
#     if request.method == "POST":
#         form = UpdateUserForm(request.POST)
        

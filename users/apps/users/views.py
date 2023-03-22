from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
# Create your views here.

class UserRegisterview(FormView):
    template_name = 'user/user.html'
    form_class = UserRegisterForm
    success_url = '/'
    
    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            #form.cleaned_data['password2'],
            #form.cleaned_data['is_staff'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            gender = form.cleaned_data['gender'],
            
        )
        
        return super(UserRegisterForm, self).form_valid(form)
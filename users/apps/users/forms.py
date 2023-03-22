from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder':'contraseña'}
            )
        )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'placeholder':'confirmar contraseña'}
        )
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'is_staff']
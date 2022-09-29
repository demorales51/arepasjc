from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=1, max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',  
        'placeholder': 'Escriba su nombre',
    }))
    
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',         
        'placeholder': 'ej: nombre@gmail.com',
    }))


    teléfono =  forms.IntegerField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control', 
       
        'placeholder': 'Escriba su teléfono',
    }))


    dirección = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control', 
         
        'placeholder': 'Escriba su dirección completa ej: int, apto',
    }))


    identificación = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control', 
        
        'placeholder': 'ID',
    }))


    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control', 
         
       
    }))


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exist():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email   
    


    def save(self):
        User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('teléfono'),
            self.cleaned_data.get('dirección'),
            self.cleaned_data.get('identificaión'), 
            self.cleaned_data.get('password'),           

        )
    

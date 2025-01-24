from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
        
        def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            
            for field_name,field in self.fields.items():
                field.widget.attrs['class']='form-control'
                field.widget.attrs['placeholder']='field-lable'
                
                
            
        
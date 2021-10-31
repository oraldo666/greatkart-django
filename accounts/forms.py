from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, EmailInput, PasswordInput
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        # widgets = {
        #     'first_name': TextInput(attrs={          ## or forms.TextInput ,,, and do not import TextInput
        #         'placeholder': 'First Name',
        #         'class': 'form-control',
        #         }),
        #     'last_name': TextInput(attrs={
        #         'placeholder': 'Last Name',
        #         'class': 'form-control',
        #     }),
        #     'phone_number': NumberInput(attrs={
        #         'placeholder': 'Enter phone number',
        #         'class': 'form-control',
        #     }),
        #     'email': EmailInput(attrs={
        #         'placeholder': 'Enter email',
        #         'class': 'form-control',
        #     }),
        #     'password': PasswordInput(attrs={
        #         'placeholder': 'Enter password',
        #         'class': 'form-control',
        #     })
        # }


    # Raise ValidationError if passwords do not match 
    def clean(self):
            cleaned_data = super(RegistrationForm, self).clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password != confirm_password:
                raise forms.ValidationError(
                    "Password does not match!!!"
                )


    # # Or the easy way to raise ValidationError:
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password != confirm_password:
    #         raise forms.ValidationError("The password does not match!!!")


    # A short adn efficient way do do all the commented script above !!!!
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'




    

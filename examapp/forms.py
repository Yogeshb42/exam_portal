from django import forms
from .models import CustomUser, ExamModel
from django.core.validators import RegexValidator
from django.conf import settings
user_model = settings.AUTH_USER_MODEL

class UserReg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,20}', message="Password should contain Minimum 8 characters, at least 1 Uppercase Alphabet, 1 Lowercase Alphabet, 1 Number and 1 Special Character")])
    username = forms.CharField(min_length=3)
    first_name = forms.CharField(min_length=3)
    last_name = forms.CharField(min_length=1)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(validators=[RegexValidator(regex=r'^[789]\d{9}$', message="Numeric Field. Only 10 digits allowed.")], max_length=10)

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already registered with us")
        return data
    
    def clean_phone(self):
        data = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=data).exists():
            raise forms.ValidationError("This phone number is already registered with us")
        return data

    class Meta:
        model = CustomUser  
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']
    
class addQuestionform(forms.ModelForm):
    class Meta:
        model = ExamModel
        fields="__all__"
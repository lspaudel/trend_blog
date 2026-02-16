# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    profile_pic = forms.ImageField(required=False, help_text='Optional. Upload your profile picture.')
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, 
                         help_text='Optional. Tell us about yourself.')
    quote = forms.CharField(max_length=255, required=False, 
                           help_text='Optional. Your favorite quote.')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
                 'profile_pic', 'bio', 'quote']
    
    def clean_email(self):
        """Validate that email is unique"""
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email
    
    def save(self, commit=True):
        """Save all CustomUser fields"""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.bio = self.cleaned_data.get('bio', '')
        user.quote = self.cleaned_data.get('quote', '')
        
        if commit:
            user.save()
            # Handle profile_pic separately since it's a file
            if self.cleaned_data.get('profile_pic'):
                user.profile_pic = self.cleaned_data['profile_pic']
                user.save()
        
        return user
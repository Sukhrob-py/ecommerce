from dataclasses import fields
from django import forms
from .models import UserProfile,Products,ContactUs

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['photo']

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=['category','message']

class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=['title','description','category','price','image','contact_name','contact_number','contact_email','contact_address']
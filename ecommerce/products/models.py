from asyncio.windows_events import NULL
from distutils.command.upload import upload
import email
from email import message
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT,related_name='user_profile')
    photo=models.ImageField(upload_to='media/',default="products/static/images/user/user.png")

    def __str__(self):
        return self.user.username


class Category(models.Model):
    category=models.CharField(max_length=120)
    def __str__(self):
        return self.category


class Products(models.Model):
    CHOICES=(
        ('Active','Active'),
        ('Sold','Sold'),
    )
    title=models.CharField(max_length=120)
    description=models.TextField()
    category=models.CharField(max_length=120)
    price=models.CharField(max_length=120)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    contact_name=models.CharField(max_length=120)
    contact_number=models.CharField(max_length=120)
    contact_email=models.CharField(max_length=120)
    contact_address=models.CharField(max_length=120)
    creator=models.ForeignKey(User,on_delete=models.PROTECT,related_name='product')
    # author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateField(auto_now=True)
    status=models.CharField(choices=CHOICES,max_length=120,default='Active')
    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    category=models.CharField(max_length=120)
    message=models.TextField()

    def __str__(self):
        return self.category

class Review(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    message=models.TextField()
    rating=models.CharField(max_length=10)
    product=models.ForeignKey(Products,on_delete=models.PROTECT,related_name='product')

    def __str__(self):
        return self.product.title+'  '+str(self.rating)
from math import prod
from pickle import FALSE
from django.shortcuts import redirect,get_object_or_404
from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserProfileForm,ProductsForm,ContactForm
from .models import Products,UserProfile,Category,ContactUs,Review

# Create your views here.
import random
######## Home page ##########
def index(request):
    products=Products.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        location=request.POST['location']
        if len(title)>0:
            products=Products.objects.filter(title=title)

        if len(category)>0:
            products=Products.objects.filter()

        if len(location)>0:
            products=Products.objects.filter(contact_address=location)

        if len(title)>0 and len(category)>0:
            products=Products.objects.filter(title=title)

        if len(location)>0 and len(title)>0:
            products=Products.objects.filter(title=title,contact_address=location)

        if len(location)>0 and len(category)>0:
            products=Products.objects.filter(contact_address=location)
        
        if len(location)>0 and len(category)>0 and len(title)>0:
            products=Products.objects.filter(contact_address=location,title=title)
    category=Category.objects.all()[:8]
    context={'products':[products],'category':{}}
    for i in category:
        product_num=Products.objects.filter(category=i.category).count()
        context['category'][i]=product_num
    
    return render(request, 'index.html',context)

###### dashboard page ########
def dashboard(request):
    products=Products.objects.filter(creator=request.user)
    user_profile=UserProfile.objects.filter(user=request.user)
    return render(request, 'dashboard.html',{'user_profile':user_profile,'products':products})

def delete(request,id):
    item=get_object_or_404(Products, id=id) 
    item.delete()
    return redirect('dashboard')
    
######### add listing page  ##########
def add_listing(request):
    category=Category.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        category=request.POST['category']
        price=request.POST['price']
        image=request.FILES['image']
        contact_name=request.POST['contact_name']
        contact_number=request.POST['contact_number']
        contact_email=request.POST['contact_email']
        contact_address=request.POST['contact_address']
        creator=request.user
        if image and len(contact_name)>0:
            data=Products(title=title,description=description,price=price,category=category,image=image,contact_name=contact_name,contact_email=contact_email,contact_address=contact_address,contact_number=contact_number,creator=creator)
            data.save()
            return redirect('dashboard')
    return render(request, 'Ad-listing.html',{'category':category})

########### user profile  ########
def user_profile(request):
    try:
        if request.method=='POST':
            imag=request.FILES['phot']
            user=request.user
            if imag:
                print('imag iiii imag')
                profile_data=UserProfile.objects.filter(user=user)
                if len(profile_data)>0:
                    profile_data.delete()
                    data=UserProfile(user=user,photo=imag)
                    data.save()
                    return redirect('user_profile')
                else:
                    data=UserProfile(user=user,photo=imag)
                    data.save()
                    return redirect('user_profile')
    except Exception as a:
        pass
    usr = User.objects.get(username=request.user.username)
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    old_password = request.POST.get('old_password', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    if len(first_name) > 0:
        usr.first_name = first_name
        usr.save()
        # return redirect('user-profile')
    if len(last_name) > 0:
        usr.last_name = last_name
        usr.save()
        # return redirect('user-profile')
    if len(old_password)>0:
        if password1==password2:
            usr.set_password(password1)
            usr.save()
            print('saqlandi')

    user_photo=UserProfile.objects.filter(user=request.user)
    return render(request, 'user-profile.html',{'user_photo':user_photo})

def single(request,id):
    product=Products.objects.get(id=id)
    user_profile=UserProfile.objects.get(user=product.creator)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        rating=request.POST['rating']
        if len(name)>0 and len(message)>0:
            prod=Review(name=name,email=email,message=message,rating=rating,product=product)
            prod.save()
            print('saqqlanddi')
            
    return render(request,'single.html',{'product':product,'user_profile':user_profile})

def category(request):
    products=Products.objects.all()
    num=Products.objects.all().count()
    results="All Products"
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        location=request.POST['location']
        if len(title)>0:
            products=Products.objects.filter(title=title)
            num=Products.objects.filter(title=title).count()
        if len(category)>0:
            products=Products.objects.filter(category=category)
            num=Products.objects.filter(category=category).count()
        if len(location)>0:
            products=Products.objects.filter(contact_address=location)
            num=Products.objects.filter(contact_address=location).count()
        
        if len(title)>0 and len(category)>0:
            products=Products.objects.filter(title=title,category=category)
            num=Products.objects.filter(title=title,category=category).count()

        if len(location)>0 and len(title)>0:
            products=Products.objects.filter(title=title,contact_address=location)
            num=Products.objects.filter(title=title,contact_address=location).count()

        if len(location)>0 and len(category)>0:
            products=Products.objects.filter(contact_address=location,category=category)
            num=Products.objects.filter(contact_address=location,category=category).count()
        
        if len(location)>0 and len(category)>0 and len(title)>0:
            products=Products.objects.filter(contact_address=location,category=category,title=title)
            num=Products.objects.filter(contact_address=location,category=category,title=title).count()
        result=title+' '+category+' '+location
        if len(result)>2:
            results=result
    category=Category.objects.all()[:8]
    context={'products':products,'results':results,'num':num,'category':{}}
    for i in category:
        product_num=Products.objects.filter(category=i.category).count()
        context['category'][i]=product_num
    return render(request,'category.html',context)

###### edit product #########
def edit_product(request,id):

    product=get_object_or_404(Products,id=id)
    category=Category.objects.all()
    status=True
    if request.method=='POST':
        product.title=request.POST['title']
        product.description=request.POST['description']
        product.price=request.POST['price']
        try:
            image=request.FILES['image']
            if image:
                product.image=request.FILES['image']
        except:
            pass
        product.category=request.POST['category']
        product.contact_address=request.POST['contact_address']
        product.contact_email=request.POST['contact_email']
        product.contact_name=request.POST['contact_name']
        product.contact_number=request.POST['contact_number']
        if product.status=='Active':
            status=True
        else:
            status=False
        product.status=request.POST['status']
        product.save()
        return redirect('dashboard')
    return render(request,'edit_product.html',{'category':category,'product':product,'status':status})

# about us
def aboutus(request):
    users=User.objects.all().count()
    context={'users':users}
    return render(request,'about-us.html',context)


def contactus(request):
    category=Category.objects.all()
    context={}
    context['category']=category
    if request.method=='POST':
        
        message=request.POST['message']
        category=request.POST['category']
        if len(message)>0 and len(category)>0:
            contact=ContactUs(name=request.user.first_name,email=request.user.email,message=message,category=category)
            contact.save()
            return redirect('contactus')
    return render(request,'contact-us.html',context)


def store(request):
    return render(request,'store.html')

def blog(request):
    return render(request,'blog.html')

def single_blog(request):
    return render(request,'single-blog.html')

def terms_condition(request):
    return render(request,'terms-condition.html')

def page_404(request):
    return render(request,'404.html')

def package(request):
    return render(request,'package.html')




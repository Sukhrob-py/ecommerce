from django.contrib import admin

from .models import UserProfile,Products,Category,ContactUs,Review
admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(ContactUs)
admin.site.register(Review)
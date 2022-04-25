from urllib.parse import urlparse
from django.urls import path
from .views import (index,dashboard,add_listing,user_profile,
                    delete,single,category,edit_product,aboutus,
                    contactus,single_blog,store,blog,terms_condition,
                    package,page_404)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',index,name='index'),
    path('dashboard',dashboard,name='dashboard'),
    path('add_listing',add_listing,name='add_listing'),
    path('user_profile',user_profile,name='user_profile'),
    path('delete/<int:id>/',delete,name='delete'),
    path('single/<int:id>',single,name='single'),
    path('category',category,name='category'),
    path('aboutus',aboutus,name='aboutus'),
    path('contactus',contactus,name='contactus'),
    path('single_blog',single_blog,name='single_blog'),
    path('store',store,name='store'),
    path('blog',blog,name='blog'),
    path('package',package,name='package'),
    path('page_404',page_404,name='page_404'),
    path('terms_condition',terms_condition,name='terms_condition'),
    path('edit_product/<int:id>',edit_product,name='edit_product'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
"""college_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path #,include
from main_page import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('accounts/',include('django.contrib.auth.urls')),
    path('home/',views.first),
    path('home/login.html',views.login_f),
    path('home/score.html',views.score),
    path('home/time_table.html',views.time_table),
    path('home/fees.html',views.fee),
    path('home/attendance.html',views.attendance),
    path('home/tutor.html',views.tutor),
     path('home/contact.html',views.contact)
    
    #path('home/student_login.html',views.student_log),
    #path('home/student_login_top.html',views.student_login_top),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

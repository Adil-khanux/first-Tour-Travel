"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from  firstproject import views
urlpatterns = [


    path('course/', views.course),
    path('course/<int:courseid>/', views.courseDetails),
    path('blog/', views.Blogs),
    path('blog/<name>', views.insideBlog),
   
   
    path('admin/', admin.site.urls),
    path('', views.homePage,name='home'),
    path('about-us/', views.aboutUs,name='about'),
    path('help/', views.helpPage,name='help'),
    path('service/', views.servicePage,name='service'),
    path('contact/', views.contactPage,name='contact'),
    path('service/<trip>', views.tripleh),
    path('form/', views.userform),
    path('submitform/',views.submitform,name='submitform'),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('marksheet/', views.marksheet),
    path('newsdetails/<newsid>',views.newsdetails),


    







   
    

   
   ]

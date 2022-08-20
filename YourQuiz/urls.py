"""YourQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from catalog import views
"""path('next/<int:todo_pk>', views.next,name='next'),
    path('next/<int:todo_pk>', views.next2,name='next2'),"""
urlpatterns = [

    path('', views.home,name='home'),
    path('mallu/', views.mallu,name='mallu'),
    path('next/', views.next,name='next'),
    path('blue/', views.blue,name='blue'),
    path('505/', views._505_,name='_505_'),


    path('admin/', admin.site.urls),
]

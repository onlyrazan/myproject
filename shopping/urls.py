"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from phone import views 
from Computers import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path('showphone/',views.showphone,name='showphone'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_logut/',views.auth_logout,name='auth_logout'),
    path('checkout/<int:id>/',views.checkout,name='checkout'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name='add_to_cart'),
    path('showcomputers/',v1.showcomputers,name='showcomputers'),
    path('detail/<int:id>/',v1.detail,name='detail'),
    path('checkoutt/<int:id>/',v1.checkoutt,name='checkoutt'),
    path('addcart/<int:id>/',v1.addcart,name='addcart')


    
]




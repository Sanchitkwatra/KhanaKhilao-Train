"""hungry_no_more URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from Hungry_No_More import views as appview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Hungry_No_More.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/',appview.SignUpView.as_view(),name='signup'),
    path('accounts/signup/vendor/', appview.VendorSignUpView.as_view(), name='vendor_signup'),
    path('accounts/signup/ngo/', appview.NGOSignUpView.as_view(), name='ngo_signup'),
    path('khanakhilao/',include('Hungry_No_More.urls')),
]

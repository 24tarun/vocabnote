"""
URL configuration for VocabNoteProject project.

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
from django.urls import path,include, re_path
from django.shortcuts import redirect
from django.conf.urls import handler404

# Custom handler for 404 errors
def redirect_to_login(request, exception=None):
    return redirect('login')

handler404 = 'vocabnoteproject.urls.redirect_to_login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("firstapp.urls")),
    path('accounts/', include('accounts.urls')),
    re_path(r'^.*$', lambda request: redirect('login')),
]

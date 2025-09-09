from django.contrib import admin
from django.urls import path,include, re_path
from django.shortcuts import redirect
from django.conf.urls import handler404

# Custom handler for 404 errors
def redirect_to_login(request, exception=None):
    return redirect('login')

handler404 = 'baseapp.urls.redirect_to_login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("vocabularyfunctions.urls")),
    path('accounts/', include('accounts.urls')),
    path('quiz/', include('quizapp.urls')),
    re_path(r'^.*$', lambda request: redirect('login')),
]

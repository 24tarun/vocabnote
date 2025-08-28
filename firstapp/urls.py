from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),
    path('options/', views.options_view, name='options'),
    path('enter_data/', views.enter_data_view, name='enter_data'),
]
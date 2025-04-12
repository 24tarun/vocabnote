from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/options/', permanent=False)),
    path('options/', views.options_view, name='options'),
    path('enter_data/', views.enter_data_view, name='enter_data'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('success/', views.success_view, name='success'),
]


from django.urls import path
from . import views

app_name = 'quizapp'

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
]

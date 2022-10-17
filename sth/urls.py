from django.urls import path
from . import views

urlpatterns = [
    path('multi/', views.MultiView.as_view(), name='multi')
]

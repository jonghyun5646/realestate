from django.urls import path
from . import views

urlpatterns = [
    path('anal/', views.AnalView.as_view(), name='anal'),
    path('pred/', views.PredView.as_view(), name='pred'),
]

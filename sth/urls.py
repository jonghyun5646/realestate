from django.urls import path
from . import views

urlpatterns = [
    path('apt/', views.AptView.as_view(), name='apt'),
    path('office/', views.OfficeView.as_view(), name='office'),
    path('multi/', views.MultiView.as_view(), name='multi')
]

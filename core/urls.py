from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('documentation/', views.documentation, name='documentation'),
    path('code-explorer/', views.code_explorer, name='code_explorer'),
    path('results/', views.results, name='results'),
    path('gallery/', views.gallery, name='gallery'),
]

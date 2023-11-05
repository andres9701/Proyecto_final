"""
URL configuration for proyect_banc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from banc.views import APIViewPersona

from django.urls import path
#router = DefaultRouter()





urlpatterns = [
    
    #url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('create-persona/', APIViewPersona.as_view(), name='create-persona'),
    path('api-delete-persona/', APIViewPersona.as_view(), name='delete-persona'),
    path('api-list-persona/<int:pk>/', APIViewPersona.as_view(), name='list-persona'),
    path('delete/<int:pk>/', APIViewPersona.as_view(), name='PersonDelete'),
    path('api-update-persona/<int:pk>/', APIViewPersona.as_view(), name='PersonUpdate'),

    #url(r'^esvyda/patient-medication/create/$',
     #   CreatePersona.as_view(), name='esvyda-patient-medication-create'),



    #path('', views.Persona_list, name='PersonList'),
    #path('create/', views.Persona_create, name='CreatePersona'),
    #path('update/<int:pk>/', views.Persona_update, name='PersonUpdate'),
    #path('delete/<int:pk>/', views.Persona_delete, name='PersonDelete'),
]

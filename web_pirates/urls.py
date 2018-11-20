"""web_pirates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pirates.views import *

urlpatterns = [
    path('', ListaTesourosView.as_view(), name='lista_tesouros'),
    path('novo-tesouro/', SalvarTesouro.as_view(), name='salvar_tesouro'),
    path('novo-tesouro/<int:id>', SalvarTesouro.as_view(), name='salvar_tesouro'),
    path('remover-tesouro/<int:id>/', RemoverTesouro.as_view(),name='remover_tesouro'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

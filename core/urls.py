"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dashboard.views import index
from produtos.views import produtos_index, produtos_insert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='dashboard_index'),
    path('produtos/', produtos_index, name='produtos'),
    path('produtos/insert/', produtos_insert, name='produtos_insert'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

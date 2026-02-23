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
from produtos.views import produtos_index, produtos_insert, produtos_edit, produtos_delete, categorias_insert, categorias_edit, categorias_delete
from accounts.views import user_login, user_logout, user_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='dashboard_index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('produtos/', produtos_index, name='produtos'),
    path('produtos/insert/', produtos_insert, name='produtos_insert'),
    path('<int:produto_id>/produtos/edit/', produtos_edit, name='produtos_edit'),
    path('<int:produto_id>/produtos/delete/', produtos_delete, name='produtos_delete'),
    path('categorias/insert/', categorias_insert, name='categorias_insert'),
    path('<int:categoria_id>/categorias/edit/', categorias_edit, name='categorias_edit'),
    path('<int:categoria_id>/categorias/delete/', categorias_delete, name='categorias_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

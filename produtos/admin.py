from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ['categoria']
    search_fields = ['categoria']
    ordering = ['categoria']

@admin.register(Produto)
class AdminProduto(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria']
    search_fields = ['nome', 'preco']
    ordering = ['preco']
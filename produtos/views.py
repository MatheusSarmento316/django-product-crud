from django.shortcuts import render
from .models import Produto, Categoria

# Create your views here.
def produtos_index(request):
    produtos = Produto.objects.filter(user=request.user)
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'produtos/produtos.html', {'produtos': produtos, 'categorias': categorias})
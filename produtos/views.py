from django.shortcuts import render, redirect
from .models import Produto, Categoria

# Create your views here.
def produtos_index(request):
    produtos = Produto.objects.filter(user=request.user)
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'produtos/produtos.html', {'produtos': produtos, 'categorias': categorias})

def produtos_insert(request):
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        Produto.objects.create(
            user = request.user,
            image = request.FILES.get('image'),
            nome = request.POST.get('nome'),
            descricao = request.POST.get('descricao'),
            preco = request.POST.get('preco'),
            categoria = categoria
        )
        return redirect('produtos')
    produtos = Produto.objects.filter(user=request.user)
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'produtos/produtos_insert.html', {'categorias': categorias, 'produtos': produtos})
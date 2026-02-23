from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Produto, Categoria

# Create your views here.
@login_required
def produtos_index(request):
    produtos = Produto.objects.filter(user=request.user)
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'produtos/produtos.html', {'produtos': produtos, 'categorias': categorias})

@login_required
def categorias_insert(request):
    if request.method == 'POST':
        Categoria.objects.create(
            user = request.user,
            image = request.FILES.get('image'),
            categoria = request.POST.get('categoria')
        )
        return redirect('produtos')
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'produtos/categorias_insert.html', {'categorias': categorias})

@login_required
def categorias_edit(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id, user=request.user)
    if request.method == 'POST':
        categoria.image = request.FILES.get('image')
        categoria.categoria = request.POST.get('categoria')
        categoria.save()
        return redirect('produtos')
    return render(request, 'produtos/categorias_edit.html', {'categoria': categoria})

@login_required
def categorias_delete(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id, user=request.user)
    categoria.delete()
    return redirect('produtos')

@login_required
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

@login_required
def produtos_edit(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, user=request.user)
    categorias= Categoria.objects.filter(user=request.user)
    if request.method == 'POST':
        categoria = get_object_or_404(Categoria, id=request.POST.get('categoria'), user=request.user)
        produto.image = request.FILES.get('image')
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.categoria = categoria
        produto.save()
        return redirect('produtos')
    return render(request, 'produtos/produtos_edit.html', {'produto': produto, 'categorias': categorias})

@login_required 
def produtos_delete(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, user=request.user)
    produto.delete()
    return redirect('produtos')
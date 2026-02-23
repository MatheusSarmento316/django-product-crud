from django.shortcuts import render, redirect, get_object_or_404



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

def produtos_delete(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, user=request.user)
    produto.delete()
    return redirect('produtos')
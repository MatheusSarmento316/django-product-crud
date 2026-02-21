from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Categoria(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categorias')
    image = models.ImageField(upload_to='categorias/')
    categoria = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria']
    
    def __str__(self):
        return self.categoria
    
class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    image = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['preco']

    def __str__(self):
        return self.nome
from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']


class Brand (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'Marca'
        ordering = ['id']



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.IntegerField (verbose_name='Precio')
    #creación de la llave:
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    #brand = models.TextField(verbose_name='Marca')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']



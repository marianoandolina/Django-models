from django.db import models
from django.contrib.auth.models import User

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:
# from django.contrib.auth.models import User


# Create your models here.
class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)

    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel id', null=False, blank=False, unique=True
    )

    title = models.CharField(
        verbose_name='title', max_length=120, default=''
    )

    description = models.TextField(verbose_name='description', default='')

    price = models.FloatField(
        verbose_name='price', max_length=5, default=0.00
    )

    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0
    )

    picture = models.URLField(verbose_name='picture', default='')

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics'
        verbose_name = 'comic'
        verbose_name_plural = 'comics'

    def __str__(self):
        '''
        El método __str__ cumple una función parecida a __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.title} - {self.id}'

class WishList(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    comic = models.ForeignKey(Comic, verbose_name='Comic', default=1, blank=True, on_delete=models.CASCADE)

    favorite = models.BooleanField(default=False)

    cart = models.BooleanField(default=False)

    wished_qty = models.PositiveIntegerField(null=True, blank=True)

    bought_qty = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'whish_list'
        verbose_name = 'whish_list'

    def __str__(self):
        return f'{self.user} - {self.comic}'    
        




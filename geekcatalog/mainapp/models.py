from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    name = models.CharField(verbose_name='название товара', max_length=128)
    receipt_date = models.DateTimeField(verbose_name='дата поступления', auto_now_add=True)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2, default=0)
    unit = models.CharField(verbose_name='единица измерения', max_length=64)
    supplier = models.CharField(verbose_name='наименование поставщика', max_length=128)

    def __str__(self):
        return f"{self.name})"

# Create your models here.

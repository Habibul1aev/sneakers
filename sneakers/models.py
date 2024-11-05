from django.db import models
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    def __str__(self):  
        return f'{self.id}) {self.name}'



class Sneakers(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    photo = models.ImageField(verbose_name='Фото', upload_to='imgs/')
    code = models.CharField(max_length=7, verbose_name='артикул')
    price = models.CharField(max_length=12, verbose_name = 'Цена')
    size = models.ManyToManyField('sneakers.Size', related_name='sneakers', verbose_name='размеры')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, related_name='sneakers', verbose_name='категория')
    seazon = models.ForeignKey('Seazon', on_delete = models.PROTECT, related_name='sneakers', verbose_name='сезон')
    color = models.ForeignKey('Color', on_delete = models.PROTECT, related_name='sneakers', verbose_name='цвет')
    category_sneakers = models.ForeignKey('CategorySneakers', on_delete = models.PROTECT, related_name='sneakers', verbose_name='категория кроссовок')
    brends = models.ForeignKey('Brends', on_delete = models.PROTECT, related_name='sneakers', verbose_name='бренд')

    def __str__(self):
        return f'{self.id}) {self.name}'

    

class Size(models.Model):
    size = models.CharField(max_length=2, verbose_name='размер')    

    def __str__(self):
        return self.size


class Seazon(models.Model):
    sezon = models.CharField(max_length=20, verbose_name='сезон')

    def __str__(self) -> str:
        return self.sezon
    

class Color(models.Model):
    color = models.CharField(max_length=20, verbose_name='цвет')

    def __str__(self) -> str:
        return self.color
    

class CategorySneakers(models.Model):
    name = models.CharField(max_length=20, verbose_name='категория кроссовок')

    def __str__(self) -> str:
        return self.name
    

class Brends(models.Model):
    name = models.CharField(max_length=20, verbose_name='бренд')

    def __str__(self) -> str:
        return self.name
    

class ImgAttribute(models.Model):
    product = models.ForeignKey('Sneakers', models.CASCADE, related_name='images', verbose_name='товар')
    image = ResizedImageField('изображение', upload_to='product_images/', quality=90, force_format='WEBP')

    def __str__(self):
        return f'{self.product.name}'




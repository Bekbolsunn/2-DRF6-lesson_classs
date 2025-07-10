from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

STARS =(
    (i,"⭐" * i) for i in range(1,6)
)

class Review(models.Model):
    text = models.TextField(null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)
    def __str__(self):
        return f'Отзыв на {self.product.title}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

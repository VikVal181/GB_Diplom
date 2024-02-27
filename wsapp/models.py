from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class Type(models.Model):
    title_t = models.CharField(max_length=30, verbose_name='Название',)

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы тура'

    def __str__(self):
        return self.title_t


class Subtype(models.Model):
    title_subt = models.CharField(max_length=30, verbose_name='Название',)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип тура')

    class Meta:
        verbose_name = 'Направление тура'
        verbose_name_plural = 'Направления туров'

    def __str__(self):
        return self.title_subt


class Product(models.Model):
    title_pr = models.CharField(max_length=70, verbose_name='Название',)
    date_start = models.DateField(default=now, editable=True, verbose_name='Дата начала тура')
    date_finish = models.DateField(default=date_start, editable=True, verbose_name='Дата окончания тура')
    difficulte = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(100),MinValueValidator(1)], verbose_name='Сложность');
    numbers = models.PositiveIntegerField(verbose_name='Количество мест',)
    description_pr = models.CharField(max_length=500, verbose_name='Описание',)
    image = models.FileField(null=True, blank=True, upload_to='static/products/', verbose_name='Изображение',)
    subtype = models.ForeignKey(Subtype, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подтип')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип')

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Тур'

    def __str__(self):
        return self.title_pr


class Order(models.Model):
    status = models.CharField(max_length=30, verbose_name='Статус заказа', )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.pk)


class DetailOrder(models.Model):
    amount_do = models.PositiveIntegerField(verbose_name='Количество', )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, db_index=False, null=True, blank=True, verbose_name='Товар')
    person = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False, null=True, blank=True, verbose_name='Юзер')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, db_index=False, null=True, blank=True, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
        unique_together = ('person', 'product', 'order')
        constraints = [
            models.UniqueConstraint(fields=['person', 'product', 'order'], name='person_product_order'),
        ]


class Review(models.Model):
    mark = models.PositiveIntegerField(verbose_name='Оценка', )
    review = models.CharField(max_length=100, verbose_name='Отзыв', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Товар')
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Юзер')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.mark)



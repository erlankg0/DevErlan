from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name Categories', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-name']


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Наименования')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата пуб.')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата измен')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изобр')
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newses'
        ordering = ['-title']

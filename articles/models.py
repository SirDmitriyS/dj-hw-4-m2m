from django.db import models


class Tag(models.Model):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    name = models.CharField(max_length=20, verbose_name='Название тега')

    def __str__(self) -> str:
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статьи', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Теги', related_name='tags')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        ordering = ['-is_main', 'tag']
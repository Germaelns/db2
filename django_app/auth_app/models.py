from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images', verbose_name="Изображение", null=True, blank=True)
    text = models.TextField(max_length=2000, verbose_name="Содержимое")
    author = models.CharField(max_length=100, verbose_name="Автор")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(max_length=400, verbose_name="Коментарий")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"



# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Kategori Adı")
    image = models.URLField(verbose_name="Kategori Resmi")
    description = models.TextField(verbose_name="Açıklama")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name="Oyun Adı")
    slug = models.SlugField(unique=True, blank=True)
    video_url = models.URLField(verbose_name="Video URL (YouTube)")
    download_url = models.URLField(verbose_name="İndirme/Satın Alma Linki")
    description = models.TextField(verbose_name="Oyun Açıklaması")
    poster_image = models.URLField(verbose_name="Poster Resmi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="games")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Oyun"
        verbose_name_plural = "Oyunlar"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class GameImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Resim Açıklaması")
    image_url = models.URLField(verbose_name="Resim URL")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="images")
    order = models.IntegerField(default=0, verbose_name="Sıra")

    class Meta:
        verbose_name = "Oyun Resmi"
        verbose_name_plural = "Oyun Resimleri"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.game.title} - {self.title}"







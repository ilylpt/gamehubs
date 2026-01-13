

# Register your models here.
from django.contrib import admin
from .models import Category, Game, GameImage


class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 3
    fields = ['title', 'image_url', 'order', 'is_active']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'game_count']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    ordering = ['title']

    def game_count(self, obj):
        return obj.games.count()
    game_count.short_description = 'Oyun Sayısı'


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']
    inlines = [GameImageInline]

    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Medya', {
            'fields': ('poster_image', 'video_url')
        }),
        ('Detaylar', {
            'fields': ('description', 'download_url')
        }),
    )


@admin.register(GameImage)
class GameImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'game', 'order', 'is_active']
    list_filter = ['is_active', 'game']
    search_fields = ['title', 'game__title']
    ordering = ['game', 'order']

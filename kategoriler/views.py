

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Game


@login_required
def categories_list(request):
    """Tüm kategorileri listele"""
    categories = Category.objects.all()
    return render(request, 'oyunlar/categories_list.html', {
        'categories': categories
    })


@login_required
def category_detail(request, slug):
    """Bir kategorinin detayını ve oyunlarını göster"""
    category = get_object_or_404(Category, slug=slug)
    games = category.games.all()
    return render(request, 'oyunlar/category_detail.html', {
        'category': category,
        'games': games
    })


@login_required
def game_detail(request, category_slug, game_slug):
    """Bir oyunun detayını göster"""
    category = get_object_or_404(Category, slug=category_slug)
    game = get_object_or_404(Game, slug=game_slug, category=category)
    images = game.images.filter(is_active=True)

    # Video URL'ini YouTube embed formatına çevir
    video_embed_url = game.video_url
    if 'youtube.com/watch?v=' in video_embed_url:
        video_id = video_embed_url.split('watch?v=')[-1].split('&')[0]
        video_embed_url = f'https://www.youtube-nocookie.com/embed/{video_id}'
    elif 'youtu.be/' in video_embed_url:
        video_id = video_embed_url.split('youtu.be/')[-1].split('?')[0]
        video_embed_url = f'https://www.youtube-nocookie.com/embed/{video_id}'
    elif 'youtube.com/embed/' in video_embed_url:
        video_embed_url = video_embed_url.replace('youtube.com', 'youtube-nocookie.com')

    return render(request, 'oyunlar/game_detail.html', {
        'game': game,
        'category': category,
        'images': images,
        'video_embed_url': video_embed_url
    })

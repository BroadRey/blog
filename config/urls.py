from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config import settings

from posts.views import hashtags_view, main_page_view, post_create_view, post_detail_view, posts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view, name='home'),
    path('posts/', posts_view, name='posts'),
    path('hashtags/', hashtags_view, name='hashtags'),
    path('posts/<int:id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

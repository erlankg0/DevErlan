from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomeNews, CategoryList, DetailNews, CreatNews, test, register, login

urlpatterns = [
    path('', HomeNews.as_view(), name="home"),
    path('category/<int:pk>/', CategoryList.as_view(), name='category'),
    path("news/<int:pk>/", DetailNews.as_view(), name="view_news"),
    path("news/add_news/", CreatNews.as_view(), name='add_news'),
    path('test/', test, name='test'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, re_path

from backend.article.views import ArticleListView, ArticleDetailView

urlpatterns = [
    re_path(r'^articles/$', ArticleListView.as_view(), name='article_list'),
    re_path(r'^articles/(?P<slug>[\w-]+)/$', ArticleDetailView.as_view(),
            name="article_detail")
]
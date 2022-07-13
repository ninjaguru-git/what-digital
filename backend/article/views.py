# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from backend.article.models import Article


class ArticleListView(ListView):
    """Article List View."""
    model = Article
    context_object_name = "article_list"
    template_name = "article/article_list.html"
    paginate_by = 2

    def get_queryset(self):
        filter_tags = self.request.GET.get('filter', None)
        qs = super(ArticleListView, self).get_queryset()
        if filter_tags:
            tags_list = filter_tags.strip().split(",")
            tags = list(map(lambda x: x.strip(), tags_list))
            qs = qs.filter(tags__name__in=tags)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["TRUNCWORDS_COUNT"] = 20
        context["filter"] = self.request.GET.get('filter', None)
        return context


class ArticleDetailView(DetailView):
    """Article Detail View."""
    model = Article
    context_object_name = "article"
    slug_field = "slug"
    template_name = "article/article_detail.html"

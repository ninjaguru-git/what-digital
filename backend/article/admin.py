# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from backend.article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    """Article Admin."""
    list_display = ("title",  "tag_list", "creation_date",)
    list_filter = ("tags",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        """tag list"""
        return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Article, ArticleAdmin)


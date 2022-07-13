# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils.text import slugify

from djangocms_text_ckeditor.fields import HTMLField
from taggit.managers import TaggableManager


class Article(models.Model):
    """Article Model."""
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        editable=False,
        max_length=200,
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=200,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to='uploads/',
        blank=True,
    )
    tags = TaggableManager()
    content = HTMLField(
        verbose_name=_("Content"),
        blank=True,
        null=True,
    )
    creation_date = models.DateTimeField(
        verbose_name=_("Creation Date"),
        auto_now_add=True,
    )

    def __str__(self):
        return "article-{}".format(self.slug)

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


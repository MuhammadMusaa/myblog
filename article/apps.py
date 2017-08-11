# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'article'
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, null=True)
    category = models.ForeignKey(Category,related_name='post_category', null=True)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = "Post"
 
    def __unicode__(self):
        return self.title
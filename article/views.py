# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from article.models import Category

from article.models import Post

# Create your views here.

def hello_word(request):
	return HttpResponse('Hello Word')

def nama_saya(request, nama_saya, umur):
    return HttpResponse('Hello nama saa adalah %s, umur saya adsalah %stahun' % (nama_saya, umur))	

def home(request):
	categories = Category.objects.all()
	post = Post.objects.all()
	data = {
		   'category' : categories,
		   'nama' : 'musa',
		   'post' : post,
		}
	return render(request, 'index.html', data)

		
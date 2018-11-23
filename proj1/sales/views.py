# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from sales.models import Products

# Create your views here.
def fun(a):
	products=[p.name+"," for p in Products.objects.all()]
	return HttpResponse(products)

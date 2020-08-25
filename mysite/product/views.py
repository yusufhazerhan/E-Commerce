# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from jedi.evaluate.context import instance

from home.models import Comment, CommentForm
from product.models import Product, ProductImage, Category


def detail(request, product_id):
    categoryList = Category.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    productimage = ProductImage.objects.filter(product_id=product_id)
    comments = Comment.objects.filter(product=product_id, status=1).order_by('-id')
    cform = CommentForm()
    context = {'page': 'home',
               'product': product,
               'productimage': productimage,
               'comments': comments,
               'cform': cform,
               'categoryList' : categoryList,
               }

    return render(request, 'detail.html', context)
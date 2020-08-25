from time import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Category(models.Model):
    STATUS = {
        (1, 'True'),
        (0, 'False')
    }
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    keywords = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def __str__(self):
        full_path = [self.title]

        k = self.parent

        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])




class Product(models.Model):
    STATUS = {
        (1, 'True'),
        (0, 'False')
    }
    SIZE = {
        (0, 'XS'),
        (1, 'M'),
        (2, 'L'),
        (3, 'XL'),
        (34, '34 Beden'),
        (36, '36 Beden'),
        (40, '40 Beden')

    }
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # relation with category
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.IntegerField()
    size = models.IntegerField(choices=SIZE)
    quantity = models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_cat_list(self):  # for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



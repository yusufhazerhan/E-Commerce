from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea, TextInput

# Create your models here.
from product.models import Product


class Contact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read')
    )
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Meta:
    verbose_name = "Contact Form Message"
    verbose_name_plural = "Contact Form Message"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Message'}),
        }


class Comment(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False')
    )
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=0)
    rating = models.IntegerField(choices=RATING, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'message', 'rating']
        widgets = {                                                                     #Auto create form

            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Message'}),
            'rating': TextInput(attrs={'class': 'input'}),
        }

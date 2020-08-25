from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from home.models import ContactForm, Contact, CommentForm, Comment
from order.models import ShopCart, ShopCartForm
from product.models import Category, Product, ProductImage


def index(request):
    categoryList = Category.objects.all()
    productList = Product.objects.all()
    sliderList = Product.objects.all()[0:8]
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    context = {'page': 'home',
               'categoryList': categoryList,
               'productList': productList,
               'sliderList': sliderList,
               }

    return render(request, 'index.html', context)


def login_form(request):
    if request.method == "POST":
        next_url = request.POST['next']  # get hidden url

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            context = {'hata': 'Username or password incorrect',
                       }
            return render(request, "login.html", context)
    else:
        return render(request, "login.html")


def contact_form(request):
    categoryList = Category.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contactdata = Contact()
            contactdata.name = form.cleaned_data['name']
            contactdata.email = form.cleaned_data['email']
            contactdata.subject = form.cleaned_data['subject']
            contactdata.message = form.cleaned_data['message']
            contactdata.save()

            messages.success(request, "Your message has been sent.")
            return HttpResponseRedirect('/contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'categoryList': categoryList,
    }
    return render(request, 'contact.html', context)


def log_out(request):
    logout(request)
    return redirect('/home')


@login_required(login_url='/login')
def comment_add(request, proid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.product_id = proid
            data.user_id = current_user.id
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Your review has been sent")
            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(url)


@login_required(login_url='/login')
def comment_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    Comment.objects.filter(id=id).delete()
    messages.success(request, "Comment successfully deleted...")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def comment_list(request):
    categoryList = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user=current_user.id).order_by('-id')
    context = {

        'page': 'comments',
        'comments': comments,
        'categoryList': categoryList,
    }
    return render(request, "comment_list.html", context)


def category(request, catid):
    productList = Product.objects.filter(category_id=catid)
    categoryList = Category.objects.all()
    categoryList2 = get_object_or_404(Category, pk=catid)
    context = {

        'page': 'products',
        'productList': productList,
        'categoryList': categoryList,
        'categoryList2': categoryList2,
    }
    return render(request, 'category.html', context)

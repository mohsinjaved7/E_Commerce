from django.shortcuts import render,redirect,HttpResponse
from app.models import Category,Sub_category,Product,UserCreationForm,Contact,Order,Brand
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User


def Master(request):
    return render(request,'master.html')


def index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandId = request.GET.get('brand')

    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(Sub_category=category_id).order_by('-id')
    elif brandId:
        products = Product.objects.filter(brand=brandId).order_by('-id')
    else:
        products = Product.objects.all()

    context = {
        'category': category,
        'products': products,
        'brand':brand,
    }
    return render(request,'index.html',context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request,'registration/signup.html',context)


@login_required(login_url="/accounts/login/")
def cart_add(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('index')


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail')


@login_required(login_url="/accounts/login/")
def item_decrement(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product)
    return redirect('cart_detail')


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request,'cart/cart_detail.html')


def ContactPage(request):
    if request.method == "POST":
        contact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        contact.save()
    return render(request,'contact_us.html')

def Checkout(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        print(cart)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
            order = Order(
                user=user,
                image=cart[i]['image'],
                product=cart[i]['name'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                address=address,
                phone=phone,
                pincode=pincode,
                total=total,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')

    return HttpResponse("this is checkout page")


def Your_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)
    context = {
        'order': order,
    }
    return render(request,'order.html',context)


def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandId = request.GET.get('brand')

    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(Sub_category=category_id).order_by('-id')
    elif brandId:
        products = Product.objects.filter(brand=brandId).order_by('-id')
    else:
        products = Product.objects.all()

    context = {
        'category': category,
        'products': products,
        'brand': brand,
    }

    return render(request,'product.html',context)


def Product_Detail(request,id):
    product = Product.objects.filter(id=id).first()
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandId = request.GET.get('brand')

    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(Sub_category=category_id).order_by('-id')
    elif brandId:
        products = Product.objects.filter(brand=brandId).order_by('-id')
    else:
        products = Product.objects.all()
    context = {
        'category': category,
        'products': products,
        'product': product,
        'brand': brand,
    }
    return render(request,'product_detail.html',context)


def search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains=query)
    context = {
        'product':product,
    }
    return render(request,'search.html',context)
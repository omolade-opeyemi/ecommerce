from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum, F
from .filters import productFilter
from django.contrib.auth.decorators import login_required

# Create your views here
aggregate=0
amt=0
spec = Product.objects.filter(prod_discount__gt=20)

def search(request):
    product=Product.objects.all()
    myFilter= productFilter(request.GET, queryset=product)
    product=myFilter.qs
    return myFilter

def homePage(request):
    twenty = Product.objects.filter(twenty_percent_discount=True)
    genres = Category.objects.all()
    myFilter=search(request)
    disc = Product.objects.filter(prod_discount__lt=20)
    spec = Product.objects.filter(prod_discount__gt=20)
    product=Product.objects.all().exclude(twenty_percent_discount=True)
    product = product.order_by('-date')
    context = {'spec':spec,'disc':disc,'amt':amt,'product':product,'myFilter':myFilter,'genres':genres,'aggregate':aggregate,'twenty':twenty}
    return render(request, 'index.html', context)

def productPage(request):
    genres = Category.objects.all()
    product=Product.objects.all()
    myFilter= productFilter(request.GET, queryset=product)
    product=myFilter.qs
    count=myFilter.qs.count()
    context={"product":product,'myFilter':myFilter,'amt':amt,'genres':genres, 'count':count,'aggregate':aggregate}
    return render(request, 'products.html', context)

def categoryPage(request, pk):
    myFilter=search(request)
    genres = Category.objects.all()
    product = Product.objects.filter(category_id=pk)
    count = product.count()
    context={"product":product,'myFilter':myFilter,'amt':amt,'genres':genres,'aggregate':aggregate,'count':count}
    return render(request, 'products.html', context)


@login_required(login_url='login')
def increasePage(request, pk):
    update = Cart.objects.get(id=pk)
    qty = update.qnty
    y = qty+1
    update.qnty=qty+1
    price = (update.unit_price)*float(y)
    discount = (update.product.prod_discount)*float(y)
    tax = 0.075 * price
    total = price - discount + tax
    update.price=price
    update.discount=discount
    update.tax=tax
    update.total=total
    update.save()
    return redirect('summary')

@login_required(login_url='login')
def reducePage(request, pk):
    update = Cart.objects.get(id=pk)
    qty = update.qnty
    y = qty-1
    update.qnty=qty-1
    price = (update.unit_price)*float(y)
    discount = (update.product.prod_discount)*float(y)
    tax = 0.075 * price
    total = price - discount + tax
    update.price=price
    update.discount=discount
    update.tax=tax
    update.total=total
    update.save()
    return redirect('summary')

def detailPage(request, pk):
    genres = Category.objects.all()
    myFilter=search(request)
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        user = request.user
        qnty = request.POST['qty']
        color = request.POST['colour']
        unit_price = product.prod_price
        price = (product.prod_price)*float(qnty)
        dis = (product.prod_discount)/100
        discount = ((product.prod_price)*dis)*float(qnty)
        tax = 0.075 * price
        total = price - discount + tax
        create = Cart.objects.create(unit_price=unit_price,tax=tax,total=total, user=user,color=color,qnty=qnty,product=product, price=price, discount=discount)
        return redirect('/')
    context = {'product':product,'amt':amt,'myFilter':myFilter,'genres':genres,'aggregate':aggregate}
    return render(request, 'product_details.html', context)


@login_required(login_url='login')
def summaryPage(request):
    global aggregate
    global amt
    user = request.user
    genres = Category.objects.all()
    myFilter=search(request)
    cart = user.cart_set.all()
    amt=cart.count()
    total_price = Cart.objects.aggregate(Sum(('price'))) 
    total_discount = Cart.objects.aggregate(Sum(('discount'))) 
    total_tax = Cart.objects.aggregate(Sum(F('tax'))) 

    aggregate = (total_price['price__sum']or 0)  - (total_discount['discount__sum']or 0) + (total_tax['tax__sum']or 0)
    context={'amt':amt,'cart':cart,'total_p':total_price,
    'total_d':total_discount,'total_t':total_tax,'aggregate':aggregate,'myFilter':myFilter,'genres':genres}
    return render(request, 'product_summary.html', context)

@login_required(login_url='login')
def deletePage(request, pk):
    item = Cart.objects.get(id=pk).delete()
    return redirect('summary')

def specialOfferPage(request):
    genres = Category.objects.all()
    myFilter=search(request)
    cart = request.user.cart_set.all()
    amt=cart.count()
    twenty = Product.objects.filter(twenty_percent_discount=True)
    context = {'spec':spec,'twenty':twenty,'amt':amt,'myFilter':myFilter,'genres':genres,'aggregate':aggregate}
    return render(request, 'special_offer.html', context)

def deliveryPage(request):
    genres = Category.objects.all()
    myFilter=search(request)
    cart = Cart.objects.all()
    cart = request.user.cart_set.all()
    amt=cart.count()
    context = {'amt':amt,'myFilter':myFilter,'genres':genres,'aggregate':aggregate}
    return render(request, 'delivery.html', context)

def show_genres(request):
    return render(request, "genres.html", {'genres': Category.objects.all()})

def paymentPage(request):
    genres = Category.objects.all()
    myFilter=search(request)
    context = {'myFilter':myFilter,'genres':genres,'aggregate':aggregate,'amt':amt}
    return render(request, 'payment.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .models import *
from datetime import datetime
from django.http import HttpResponse
from datetime import datetime

def home(request):
    products = Product.objects.all().order_by('id')  

    
    product1 = products[0] 
    product2 = products[1] 
    product3 = products[2] 
    product4 = products[3] 

    return render(request, 'home.html', {
        'product1': product1,
        'product2': product2,
        'product3': product3,
        'product4': product4,
    })
def login(request):
    return render(request, 'loginpage.html')
def register(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        add(name=name,email=email,username=username,password=password).save()
        return redirect('/login/')
    return render(request,'register.html')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'checkout.html', {'product': product})

def buy_now(request, product_id):
   
    return redirect('checkout_page', product_id=product_id)

def checkout_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    qty = 1
    total = product.price * qty
    return render(request, 'checkout.html', {
        'product': product,
        'qty': qty,
        'total': total
    })

def remove_from_cart(request, id):
    cart = request.session.get("cart", {})
    product_id_str = str(id)
    
    if product_id_str in cart:
        del cart[product_id_str]
        request.session["cart"] = cart
        request.session.modified = True
        messages.success(request, "Item removed from cart!")
    
    return redirect('cart_page')
def home2(request):
    return render(request, 'home2.html')
def userlog(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
     
        cr = add.objects.filter(username=username,password=password,)

        if cr:
            user_details=add.objects.get(username=username,password=password,)
            id=user_details.id
            name=user_details.name
            email=user_details.email

            request.session['id']=id
            request.session['name']=name
            

            

            return redirect('home2')
        else:
           
            return render(request,'loginpage.html',{'error':'Incorrect username or password. Please try again.'})
    else:return render(request,'register.html')
def add_to_cart(request, id):
    if not request.session.session_key:
        request.session.create()

    product = get_object_or_404(Product, id=id)
    cart = request.session.get("cart", {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session["cart"] = cart
    request.session.modified = True 

  
    return redirect('home2') 
def cart_page(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            amount = product.price * qty
            total += amount
            cart_items.append({
                "product": product,
                "qty": qty,
                "amount": amount,
            })
        except Product.DoesNotExist:
            pass  

    cart_item_count = sum(cart.values()) if cart else 0

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total,
        "cart_item_count": cart_item_count,
    })
def home2(request):
    products = Product.objects.all().order_by('id')
    
    
    product_list = list(products)
    product1 = product_list[0] 
    product2 = product_list[1] 
    product3 = product_list[2] 
    product4 = product_list[3] 

    cart = request.session.get("cart", {})
    cart_item_count = sum(cart.values()) if cart else 0

    return render(request, 'home2.html', {
        'product1': product1,
        'product2': product2,
        'product3': product3,
        'product4': product4,
        'cart_item_count': cart_item_count,
    })
def his(request,id):
    a=request.session['id']
    b=History()
    b.product_id=id
    b.add_id=a
    b.date=datetime.today()
    b.save()
    return redirect('/home2/')


def viewhis(request):
    
    b =request.session['id']
    obj = History.objects.filter(add_id = b)
    print(obj)
    return render(request,'his.html',{'data':obj})
def pay(request):
    return render(request, 'n.html')
def payment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'payment.html', {'product': product})
def generate_invoice(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    html_content = f"""
    <html>
    <head><title>Invoice - {product.name}</title></head>
    <body style="font-family: Arial; text-align:center; padding:40px; background:#f9f9f9;">
        <h1 style="color:#000; font-size:28px;">INVOICE</h1>
        <p><strong>Order Date:</strong> {datetime.now().strftime('%d %B %Y')}</p>
        <p><strong>Customer:</strong> {request.session.get('name', 'Guest User')}</p>
        <hr style="margin:20px 0;">
        <img src="{request.build_absolute_uri(product.image.url)}" style="width:220px; border-radius:12px; margin:20px;">
        <h2 style="font-size:24px; margin:10px;">{product.name}</h2>
        <p style="font-size:18px;"><strong>Quantity:</strong> 1</p>
        <p style="font-size:20px; color:green;"><strong>Total Paid: ₹{product.price}</strong></p>
        <p style="margin-top:30px; color:#555;">Thank you for shopping with us!</p>
        <hr>
        <p style="color:#888; font-size:12px;">Nike Store • Powered by Django</p>
    </body>
    </html>
    """
    response = HttpResponse(html_content)
    response['Content-Disposition'] = f'attachment; filename="Invoice_{product.name.replace(" ", "_")}.html"'
    return response
def success(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    a=request.session['id']
    b=History()
    b.product_id=product_id
    b.add_id=a
    b.date=datetime.today()
    b.save()
    
    return render(request, 'success.html', {'product': product})
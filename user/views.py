from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from . import models
from employees import models as emplo
from orders import models as ord
from cart.forms import CartAddProductForm
from cart.cart import Cart
# Create your views here.
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    depart = emplo.Departments.objects.filter(need_emp=True)
    employ = emplo.Employees.objects.all()

    u = request.user.username

    o = ord.order.objects.filter(date=datetime.now().date()).count
    r = models.Table.objects.filter(date=datetime.now().date()).count
    co = models.Contact.objects.filter(date=datetime.now().date()).count
    ca = models.Careers.objects.filter(date=datetime.now().date()).count

    c = models.Category.objects.all()
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    for item in cart:  # تسمح لليوزر انه يعدل علي الكمية طالما العنصر مازال موجود داخل الكارت
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'home.html', {'u':u, 'o':o, 'r':r, 'co':co, 'ca':ca, 'depart':depart,'employ':employ, 'c':c, 'cart_product_form':cart_product_form, 'cart': cart,})

def product(request, slug):
    c = models.Category.objects.all()
    p = models.Product.objects.filter(slug=slug)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    for item in cart:  # تسمح لليوزر انه يعدل علي الكمية طالما العنصر مازال موجود داخل الكارت
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'home.html', {'c':c, 'p': p, 'cart_product_form':cart_product_form, 'cart': cart,})


def reserve(request):
    name = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['Phone']
    people = request.POST['People']
    date = request.POST['Date']
    time = request.POST['Time']
    message = request.POST['Message']
    new = models.Table()
    new.name = name
    new.email = email
    new.phone = phone
    new.many = people
    new.date = date
    new.time = time
    new.message = message

    if str(datetime.now().date()) < new.date:
        new.save()
        return render(request, 'reserved.html',{'table':new.id})
    else:
        return render(request, 'failed.html', {})


def reservations(request):
    return render(request, 'edit.html', {})


def reservationsFound(request):
    d = request.POST['Emaill']
    r = models.Table.objects.filter(email=d)
    now = datetime.now()
    return render(request, 'edit.html', {'r':r, 'now':now,})


def updatetable(request, id):
    d = models.Table.objects.get(id=id)
    data1 = d.name
    data2 = d.email
    data3 = d.phone
    data4 = d.many
    data5 = d.date
    data6 = d.time
    data7 = d.message
    return render(request, 'edittable.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})

def saveupdatetable(request, id):
    Name = request.POST['NAME']
    Email = request.POST['EMAIL']
    Phone = request.POST['PHONE']
    People = request.POST['PEOPLE']
    Date = request.POST['DATE']
    Time = request.POST['TIME']
    Message = request.POST['MESSAGE']
    neww = models.Table(id=id)
    neww.name = Name
    neww.email = Email
    neww.phone = Phone
    neww.many = People
    neww.date = Date
    neww.time = Time
    neww.message = Message
    if str(datetime.now().date()) < neww.date:
        neww.save()
        return render(request, 'reserved.html',{'table':neww.id})
    else:
        return render(request, 'failed.html', {})


def deletetable(request,id):
    old=models.Table(id=id)
    old.delete()
    return render(request, 'deleted.html', {})


def complaints(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    new = models.Contact()
    new.name = name
    new.email = email
    new.message = message
    new.save()
    return render(request, 'complaint.html',{})


def applying(request):
    name = request.POST['nname']
    email = request.POST['eemail']
    phone = request.POST['pphone']
    role = request.POST['role']
    work = request.POST['work']
    experience = request.POST['exp']
    cv = request.FILES['MyFile']
    new = models.Careers()
    new.name = name
    new.email = email
    new.phone = phone
    new.role = role
    new.work = work
    new.experience = experience
    new.cv = cv
    new.save()
    return render(request, 'applyed.html', {})


def inlogpage(request):
    return render(request, 'inlogpage.html',{})


def saveinlog(request):
    o = ord.order.objects.filter(date=datetime.now().date()).count
    r = models.Table.objects.filter(date=datetime.now().date()).count
    co = models.Contact.objects.filter(date=datetime.now().date()).count
    ca = models.Careers.objects.filter(date=datetime.now().date()).count

    u = request.POST['USERNAME']
    p = request.POST['PASSWORD']
    result = authenticate(username=u, password=p)
    if result is not None:
        login(request,result)
        return render(request, 'home.html',{'u':u, 'o':o, 'r':r, 'co':co, 'ca':ca})
    else:
        messages.error(request, 'User not exist, try again', extra_tags='error')
        return render(request, 'inlogpage.html',{})


def saveinlog2(request):
    u = request.POST['userNAME']
    p = request.POST['passWORD']
    result = authenticate(username=u, password=p)
    if result is not None:
        login(request,result)
        return HttpResponseRedirect('../admin/')
    else:
        return render(request, 'inlogpage.html',{})


def outlog(request):
    logout(request)
    return HttpResponseRedirect('/')




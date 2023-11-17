from django.shortcuts import render, redirect   
from .models import UplodeItemsDB
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from .forms import UplodeItems
from .forms import UplodeItems

# Create your views here.

def home(request):
    items_list = UplodeItemsDB.objects.all()[:10]
    return render(request, "display/home.html", {"items": items_list, "data" : "ALL Items"})

def Superuser(request):
    if request.method == "POST":
        username = request.POST['uname']
        passwd = request.POST['passwd']

        user = auth.authenticate(username=username, password=passwd)
        if user is not None and user.is_superuser:
            auth.login(request, user)
        else:
            messages.info(request, "Invalid credentials")
            

    return render(request, "display/superuser_menu.html")


def additems(request):
    formdata = UplodeItems()
    if request.method == "POST":
        img = request.FILES["imgfile"]
        title = request.POST["title"]
        price = request.POST["price"]
        Size = request.POST["Size"]

        if Size == "select":
            messages.info(request, "Select Size!")    
        else:
            db = UplodeItemsDB(img = img, title = title, price = price, Size = Size)
            db.save()
            messages.info(request, "Saved")
    return render(request, "display/additems.html", {"formdata" : formdata})

def deleteitems(request):
    items_list = UplodeItemsDB.objects.all()
    if request.method == "POST":
        item_id = request.POST["item"]
        UplodeItemsDB.objects.get(id = item_id).delete()
    return render(request, "display/deleteItems.html", {"items": items_list})

def logout(request):
    auth.logout(request)
    return redirect('/')


def s(request):
    items_list = UplodeItemsDB.objects.filter(Size="S")
    return render(request, "display/home.html", {"items": items_list, "data" : "Size: S"})

def m(request):
    items_list = UplodeItemsDB.objects.filter(Size="M")
    return render(request, "display/home.html", {"items": items_list, "data" : "Size: M"})

def l(request):
    items_list = UplodeItemsDB.objects.filter(Size="L")
    return render(request, "display/home.html", {"items": items_list, "data" : "Size: L"})

def xl(request):
    items_list = UplodeItemsDB.objects.filter(Size="XL")
    return render(request, "display/home.html", {"items": items_list, "data" : "Size: XL"})

def xxl(request):
    items_list = UplodeItemsDB.objects.filter(Size="XXL")
    return render(request, "display/home.html", {"items": items_list, "data" : "Size: XXL"})

def none(request):
    items_list = UplodeItemsDB.objects.filter(Size="none")
    return render(request, "display/home.html", {"items": items_list, "data" : "Others"})

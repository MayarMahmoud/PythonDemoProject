from django.shortcuts import render, get_object_or_404
from .models import product,user
from django.shortcuts import redirect
from .forms import register_form



# Create your views here.
def details(request,id):
    productDetail =get_object_or_404(product,pk=id)
    return render(request,"product/details.html",{"product":productDetail})

def getAll(request):
    return render(request,"product/product.html",{"products": product.objects.all()})

def getAllusers(request):
    return render(request,"user/user.html",{"users": user.objects.all()})


def new(request):
    form=register_form()
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = register_form()
    return render(request,"user/register.html",{"form":form})


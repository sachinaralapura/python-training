from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, "home.html")


def Products(request):
    return render(request, "products.html")


def Service(request):
    return render(request, "service.html")


def Contact(request):
    return render(request, "contact.html")


def Careers(request):
    return render(request, "careers.html")

def Base(request):
    return render(request,"base.html")

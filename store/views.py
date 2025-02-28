from django.shortcuts import render,redirect

from store.models import User

# Create your views here.

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about/about.html')

def team(request):
    return render(request,'about/team.html')

def review(request):
    return render(request,'about/review.html')

def products(request):
    return render(request,'product.html')

def blog(request):
    return render(request,'about/blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user = User(name=name,email=email,subject=subject,message=message)
        user.save()
        return redirect('index')
    return render(request,'contact.html')
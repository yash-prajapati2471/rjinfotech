from django.shortcuts import render,redirect
from store.models import subscribe

def index(request):
    if request.method == "POST":
        email = request.POST['email']

        a = subscribe(email=email)
        a.save()
        return redirect('index')
    return render(request,'index.html')

from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from .models import Users



# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, errors)

def process(request):
    if request.method == 'POST':
        errors = Users.objects.validate(request.POST)

        if not errors:
            user = Users.objects.createUse(request.POST)

        flashErrors(request, errors)
        return redirect(reverse('success'))

    return redirect('/')

def success(request):
    context = {
        'user': Users.objects.all()
    }
    return render(request, 'success', context)

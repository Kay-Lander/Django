from django.shortcuts import render, redirect, reverse
from ..login.models import User
from .models import Book

# Create your views here.
def index(request):
    current_user = User.objects.currentUser(request)

    context = {
        'user': current_user
    }
    return render(request, 'review/index.html', context)

def create(request):
    print "inside the method"

    if request.method == 'POST':
        if len(request.POST) != 0:

            current_user = User.objects.currentUser(request)
            book = Book.objects.AddBook(request.POST, current_user)
            print AddBook

    return render(request, 'review/create.html')

def review(request):

    print "inside review Meth"
    if request.method == "POST":
        if len(form_data['review']) != o:
            current_user = User.objects.current_user(request)

    return render(request, 'review/review.html')

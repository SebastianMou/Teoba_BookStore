from django.shortcuts import render, redirect
from .models import Category, Book
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

@login_required
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    context = {
        'book': book,
    }
    return render(request, 'store/book_detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books,
    }
    return render(request, 'store/category.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ('Hubo un error de inicio de sesión, inténtalo de nuevo'))
            return redirect('login')


    return render(request, 'store/users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'se desconectó con éxito')
    return redirect('home')

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def course_details(request):
    return render(request, 'store/course_details.html')

def courses(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'store/courses.html', context)

def events(request):
    return render(request, 'store/events.html')

def pricing(request):
    return render(request, 'store/pricing.html')

def trainers(request):
    return render(request, 'store/trainers.html')

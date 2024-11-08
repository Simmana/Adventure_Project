from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Place, Zapis
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Place
import requests

categories = Category.objects.all()
places = Place.objects.all()

def main_page(request):
    
    context = {
        'categories': categories,
        'places': places
    }
    return render(request, "./main.html", context)

def booking_page(request):
    zapiss = Zapis.objects.all

    context = {
        'zapiss': zapiss
    }
    return render(request, "./booking.html", context)

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    context = {
        'places': places,
        'place': place
    }
    return render(request, "./place-detail.html", context)

def profile_page(request):
    return render(request, "./profile.html")

def category_by_main_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    place = Place.objects.filter(category=category)
    context = {
        'category': category,
        'place': place,
        'categories': categories,
    }
    return render(request, "./category-by-category.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render (request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('login_page')

def search_action(request):
    query = request.GET.get('q')
    places = Place.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'places': places,
        'categories': categories
    }
    return render(request, "./results.html", context)

def salary_detail(request):
    salary = Place.objects.all()

    salary_filters = request.GET.getlist('cost')
    if salary_filters:
        if 'low' in salary_filters:
            salary = salary.filter(salary__lt=1000)
        if 'medium' in salary_filters:
            salary = salary.filter(salary__gte=1000, salary__lte=10000)
        if 'high' in salary_filters:
            salary = salary.filter(salary__gt=10000)
        if 'free' in salary_filters:
            salary = salary.filter(salary=0)


    date_filters = request.GET.getlist('date')
    if date_filters:
        salary = salary.filter(date__in=date_filters)

    context = {
        'salary': salary,
        'categories': categories
    }

    return render(request, './salary_1.html', context)

def weather_view(request):
    api_key = '9c915bd007bec8540a2cd483fce7f5cc'
    city = 'London'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + api_key
    response = requests.get(url.format(city))
    data = response.json()
    print(response.text)
    # Определение типа погоды и выбор изображения
    weather_type = data['weather'][0]['main']
    print(response.text) 
    if weather_type == 'Snow':
        image_url = './images/snezhno.png'
    elif weather_type == 'Clouds':
        image_url = './images/oblachno.png'
    elif weather_type == 'Clear':
        image_url = './images/Солнечно-1.png'
    else:
        image_url = './images/Солнечно-1.png'

    return render(request, './main.html', {'image_url': image_url})


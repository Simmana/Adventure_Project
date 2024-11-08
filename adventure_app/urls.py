from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home_page"),
    path('booking/', views.booking_page, name="booking_page"),
    path('sign-up/', views.sign_up_page, name="sign_up_page"),
    path('profile/', views.profile_page, name="profile_page"),
    path('login/', views.login_page, name="login_page"),
    path('main/category/<slug:slug>/', views.category_by_main_page, name="category_by_main_page"),
    path('logout/', views.logout_action, name="logout_action"),
    path('place/detail/<int:pk>/', views.place_detail, name="place_detail"),
    path('search/', views.search_action, name="search_action"),
    path('place/salary/', views.salary_detail, name="salary"),
    path('weather/', views.weather_view, name="weather_view")
]
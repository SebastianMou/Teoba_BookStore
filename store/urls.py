from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('item/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course_details/', views.course_details, name='course_details'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('trainers/', views.trainers, name='trainers'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from home.views import index
from company.views import about, contact
from users.views import register

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(
        template_name='logout.html'), name='logout'),
    path('register', register, name='register')
]

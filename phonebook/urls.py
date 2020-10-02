from django.urls import path
from . import views

app_name = 'phonebook'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('edit_contact/<int:id>', views.add_contact, name='edit_contact'),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),
]
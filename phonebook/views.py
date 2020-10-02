from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ContactList


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        d = ContactList.objects.filter(user=request.user).order_by('contactName')
        return render(request, 'phonebook/home.html', {
            'datas': d
        })

    return render(request, 'phonebook/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('phonebook:home'))
        else:
            return render(request, 'phonebook/login.html', {
                'message': 'Invalid credential.'
            })
    return render(request, 'phonebook/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'phonebook/login.html', {
            'message': 'Logged Out.'
        })
    return render(request, 'phonebook/login.html')


def register(request):
    if request.method == 'POST':
        if(User.objects.filter(username=request.POST['username']).exists()):
            return render(request, 'phonebook/register.html', {
                'message': 'Username is invalid',
                'username': request.POST['username'],
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'email': request.POST['email']
            })
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('phonebook:home'))
    else:
        return render(request, 'phonebook/register.html')


def add_contact(request, id=0):
    if request.user.is_authenticated:
        if id==0:
            if request.method == 'POST':
                user = request.user
                name = request.POST['name']
                email = request.POST['email']
                phone_number = request.POST['phonenumber']
                f = ContactList(user=user, contactName=name, contactEmail=email, contactNumber=phone_number)
                f.save()
                return HttpResponseRedirect(reverse('phonebook:home'))
            return render(request, 'phonebook/add_contact.html')
        else:
            if request.method == 'POST':
                f = ContactList.objects.get(id=id)
                f.contactName = request.POST['name']
                f.contactEmail = request.POST['email']
                f.contactNumber = request.POST['phonenumber']
                f.save()
                return HttpResponseRedirect(reverse('phonebook:home'))
            else:
                f = ContactList.objects.get(id=id)
                return render(request, 'phonebook/add_contact.html', {
                    'contact': f
                })
    return render(request, 'phonebook/login.html')


def delete_contact(request, id):
    if request.user.is_authenticated:
        ContactList.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('phonebook:home'))
    return render(request, 'phonebook/login.html')


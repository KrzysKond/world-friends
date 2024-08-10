from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app.forms import RegisterForm, PersonForm
from app.models import Person


def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('map')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('map')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('map')


@login_required
def map_view(request):
    if request.method == 'POST':
        if 'delete_person_id' in request.POST:
            person_id = request.POST.get('delete_person_id')
            person = get_object_or_404(Person, id=person_id, user=request.user)
            person.delete()
            return redirect('map')

        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return redirect('map')

    else:
        form = PersonForm()

    people = Person.objects.filter(user=request.user)
    current_year = datetime.now().year
    for person in people:
        person.age = current_year - person.born if person.born else None
    return render(request, 'map.html', {'form': form, 'people': people})


def people_locations(request):
    people = Person.objects.filter(user=request.user)
    data = [
        {
            'name': person.name,
            'latitude': str(person.latitude),
            'longitude': str(person.longitude),
            'origin': str(person.origin),
            'born': person.born,
            'photo': person.photo.url if person.photo else None,
            'id': person.id
        }
        for person in people
    ]
    return JsonResponse(data, safe=False)


def person_view(request, person_id):
    person = get_object_or_404(Person, id=person_id, user=request.user)

    context = {
        'person': person
    }

    return render(request, 'person_detail.html', context)

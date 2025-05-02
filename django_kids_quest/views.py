from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Book, Employee, Team, Client, Event
from .forms import BookForm, ClientForm, EventForm, TeamEventForm
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    return render(request, "home.html")

def logout_now(request):
    return HttpResponse("<h1>Вы вышли из аккаунта</h1>Приходите ещё!")

def books(request):

    return HttpResponse("Книги")

def permission_denied(request):
    return render(request, '403.html', status=403)

def book_detail(request, book_id):

    book = Book.objects.get(id=book_id)

    # response = f"Book ID: {book_id}"

    return render(request, "book_detail.html", {"book":book})

def employee_info(request, empl_id):

    empl = Employee.objects.get(id=empl_id)

    return render(request, "empl.html", {"empl":empl})

def book_create_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print(Book.objects.all())
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})

def client_create_view(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            print(Client.objects.all())
    else:
        form = ClientForm()
    return render(request, "client_form.html", {"form": form})

def event_create_view(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            print(Event.objects.all())
    else:
        form = EventForm()
    return render(request, "event_form.html", {"form": form})

def assign_team_event(request):
    if request.method == 'POST':
        form = TeamEventForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            event = form.cleaned_data['event']
            team.event = event
            team.save()
            return redirect('home')
    else:
        form = TeamEventForm()
    return render(request, 'assign_team_event.html', {'form': form})

def employee_list(request):
    query = request.GET.get("q")

    team_filter = request.GET.get("team")

    employees = Employee.objects.all()

    if query:
        employees = Employee.objects.filter(username__icontains=query)
    
    teams = Team.objects.all()

    if team_filter:
        employees = employees.filter(team__id=team_filter)

    return render(request,"empl_list.html",{'employees': employees,'teams': teams, 'selected_team': team_filter})


def event_list(request):
    events = Event.objects.all()

    date = request.GET.get("date")

    
    if date:
        date = parse_date(date)

        events = Event.objects.filter(date=date)

    
    return render(request,"event_list.html",{'events': events})

def empl(request):
    empl = Employee.objects.all()

    name = request.GET.get("username")

    print(name)

    if name:

        empl = Employee.objects.get()

    print(empl)

    return render(request, "empl.html", {"empl":empl})
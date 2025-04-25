from django import forms

from .models import Book, Client, Event, Team

class CustomBookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    extra_info = forms.CharField()

class TeamEventForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=Event.objects.all(), label="Выберите мероприятие")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',"author", "pages", "price"]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name',"birth_date", "phone_number", "email", "city"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name',"guests", "budget", "description", "date"]

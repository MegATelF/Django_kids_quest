from django.contrib import admin

from .models import Employee, User, Event, Team, Book, Client

# Register your models here.


admin.site.register(Employee)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Book)
admin.site.register(Client)
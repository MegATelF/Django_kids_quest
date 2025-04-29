"""
URL configuration for django_kids_quest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
# from django.urls import handler403
from . import views

# handler403 = view.permission_denied

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("books/", views.books, name="books"),
    path("book/<int:book_id>", views.book_detail, name="book_detail"),
    path("employee_info/<int:empl_id>", views.employee_info, name="employee_info"),
    path("empl_list/", views.employee_list, name="employees"),
    path("custom_book_create/", views.book_create_view, name="book_create"),
    path("client_form/", views.client_create_view, name="client_form"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="logout_now"), name="logout"),
    path("logout_now", views.logout_now, name="logout_now"),
    path('forbidden/', views.permission_denied, name='forbidden'),
    path("event_form/", views.event_create_view, name="event_form"),
    path("assign_team_event/", views.assign_team_event, name="assign_team_event"),
    path("event_list/", views.event_list, name="event_list"),
    path("empl/", views.empl, name="empl"),

    
]

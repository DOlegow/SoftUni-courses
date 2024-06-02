from django.urls import path
from djangoproject.phonebook import landing_page

urlpatterns = [
    path('', landing_page, name='landing-page')
]
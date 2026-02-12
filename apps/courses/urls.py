from django.urls import path

from .views import course_list

app_name = 'courses'

urlpatterns = [
    path('', course_list, name='course_list'),
]

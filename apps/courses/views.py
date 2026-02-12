from django.shortcuts import render

from .models import Course


def course_list(request):
    courses = Course.objects.select_related('teacher').prefetch_related('lessons__materials')
    return render(request, 'courses/course_list.html', {'courses': courses})

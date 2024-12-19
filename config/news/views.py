from django.shortcuts import render

# Create your views here.
from .models import Course

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})

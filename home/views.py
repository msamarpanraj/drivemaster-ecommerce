from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lesson



# Create your views here.
def index(request):
    """ A view to return the home page """
    
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        # Process form data here, e.g., save it or send an email
        messages.success(request, "Your message has been sent!")
        return redirect('contact')
    return render(request, 'home/contact.html')

def lessons(request):
    return render(request, 'home/lessons.html')

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'home/lesson_detail.html', {'lesson': lesson})
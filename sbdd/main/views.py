from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    View for the home page - displays the coming soon template
    """
    return render(request, 'main_layout.html')

def about(request):
    """
    View for about page - can be used for additional info
    """
    context = {
        'page_title': 'About SB-DD Platform'
    }
    return render(request, 'main_layout.html', context)

def contact(request):
    """
    View for contact page - placeholder for future contact form
    """
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'main_layout.html', context)
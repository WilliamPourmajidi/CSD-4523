from django.http import HttpResponse

def index(request):
    # This is the view function for the index page
    return HttpResponse("Hello, world! This is my first Django app.")

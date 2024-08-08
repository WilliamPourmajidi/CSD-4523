from django.http import HttpResponse

def hello_world(request):
    # This function will handle the HTTP request and return a response.
    return HttpResponse("Hello, World!")

from django.shortcuts import render

# Create your views here.
def homepageViews(request):
    return render(request, 'homepage.html')
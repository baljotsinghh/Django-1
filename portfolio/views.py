from django.shortcuts import render

# Create your views here.
def starter_page(request):
    return render(request, 'portfolio/starter-page.html')

def index(request):
    return render(request, 'portfolio/index.html')

def project_details(request):
    return render(request, 'portfolio/portfolio-details.html')


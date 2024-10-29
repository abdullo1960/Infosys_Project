from django.shortcuts import render

from myapp.models import MessageModel, Testimonial,TeamModel

# Create your views here.

def homePageView(request):
    testimonials = Testimonial.objects.all()
    teams = TeamModel.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        text = request.POST.get("text")
        MessageModel.objects.create(name=name, email=email, subject=subject, text=text)
    context = {
    "testimonials": testimonials,
    "teams": teams
    }
    return render(request, 'home.html', context)

def aboutPageView(request):
    return render(request, 'about.html')

def blogPageView(request):
    return render(request, 'blog.html')

def contactPageView(request):
    return render(request, 'contact.html')

def pricePageView(request):
    return render(request, 'price.html')

def servicesPageView(request):
    return render(request, 'service.html')
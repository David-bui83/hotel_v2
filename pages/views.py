from django.shortcuts import render, HttpResponse, redirect
from testimonials.models import Testimonial

# Create your views here.
def index(request):
  return render(request, 'pages/index.html')

def about(request):
  tests = Testimonial.objects.order_by('-id')[:2]
  context = {
    'tests': tests
  }
  return render(request, 'pages/about.html', context)
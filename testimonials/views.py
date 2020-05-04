from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Testimonial
import os 
# Create your views here.
def testimonial(request):
  return render(request, 'testimonials/testimonials.html')

def add_testimonial(request):
  if request.method == 'POST':
    if not request.FILES:
      messages.error(request, 'Image is required')
      return redirect('testimonial')

    errors = Testimonial.objects.basic_validator(request.POST)

    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
        return redirect('testimonial')
    else:
      postData = {
        'name': request.POST['name'],
        'email': request.POST['email'],
        'img': request.FILES['img'],
        'message': request.POST['message']
      }
    
      img = postData['img'].name.split('.')
      if img[0] != 'jpg' or img[0] != 'png':
        messages.error(request, 'Not a valid Image')
        return redirect('testimonial')

  return redirect('testimonial')
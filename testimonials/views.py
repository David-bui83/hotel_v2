from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Testimonial
import imghdr
import os 

# Create your views here.
def testimonial(request):

  testimonials = Testimonial.objects.all().order_by('-id')
  
  context = {
    'tests': testimonials
  }

  return render(request, 'testimonials/testimonials.html', context)

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

      img = imghdr.what(postData['img'])
      print('img type', img)
      # img = postData['img'].name.split('.')
      # print(img)
      if not img:
        messages.error(request, 'Not a valid Image')
        return redirect('testimonial')
      else:
        Testimonial.objects.create(name=postData['name'],email=postData['email'],img=postData['img'],testimonial=postData['message'])
        messages.success(request, 'Successfully added your testimony')
        return redirect('testimonial')


  return redirect('testimonial')
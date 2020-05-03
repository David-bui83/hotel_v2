from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.core.mail import send_mail
from .models import Message, MessageManager

# Create your views here.
def contact(request):
  return render(request, 'contacts/contacts.html')

def message(request):
  
  if request.method == 'POST':
    postData = {
      'name': request.POST['name'],
      'email': request.POST['email'],
      'message': request.POST['message']
    }

    errors = Message.objects.basic_validator(postData)
    print(errors)

    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
        
        return redirect('contact')
    else:
      Message.objects.create(name=postData['name'],email=postData['email'],message=postData['message'])

      visitor = Message.objects.last()

      send_mail(
        'Message Received',
        f'Hello {visitor.name}, Thank you for contacting us. We will get back to you ASAP',
        '',
        [''],
        fail_silently=False
      )
      
      print(visitor.name)
      value = 'Your message was received'
      messages.success(request, value)  

  return redirect('contact')
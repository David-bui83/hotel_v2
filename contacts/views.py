from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from .models import Message, MessageManager

# Create your views here.
def contact(request):
  return render(request, 'contacts/contacts.html')

def message(request):
  
  if request.method == 'POST':

    errors = Message.objects.basic_validator(request.POST)
    print(errors)

    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
        
        return redirect('contact')
    else:
      value = 'Your message was received'
      messages.success(request, value)  
  return redirect('contact')
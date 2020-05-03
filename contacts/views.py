from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from .models import Message, MessageManager

# Create your views here.
def contact(request):
  return render(request, 'contacts/contacts.html')

def message(request):
  
  if request.method == 'POST':
  #   try:
  #     name = request.POST['name']
  #     email = request.POST['email']
  #     message = request.POST['message']
  #   except:
  #     name = ''
  #     email = ''
  #     message = ''
  #   finally:
    errors = Message.objects.basic_validator(request.POST)
    print(errors)

    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
        
        return redirect('contact')
      
  return redirect('contact')
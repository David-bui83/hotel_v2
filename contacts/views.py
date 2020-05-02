from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def contacts(request):
  return render(request, 'contacts/contacts.html')
from django.urls import path
from . import views

urlpatterns = [
  path('', views.testimonial, name='testimonial'),
  path('add_testimonial', views.add_testimonial, name="add_testimonial")
]
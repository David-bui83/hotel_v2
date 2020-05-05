from django.contrib import admin
from .models import Testimonial

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'created_at')

admin.site.register(Testimonial, TestimonialAdmin)
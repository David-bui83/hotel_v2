from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import os

# Create your models here.

class TestimonialManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if len(postData['name']) < 2:
      errors['name'] = 'Name needs to have at least 2 characters'
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = 'Not a valid email'
   
    if len(postData['message']) < 10:
      errors['message'] = 'Testimonial needs to be at least 10 characters'
    return errors

class Testimonial(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
  testimonial = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TestimonialManager()

  def __str__(self):
    return f'{self.name}'
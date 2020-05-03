from __future__ import unicode_literals
from django.db import models
import re 
# Create your models here.

# Validation model
class MessageManager(models.Manager):
  
  def basic_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    if len(postData['name']) < 2:
      errors['name'] = 'Name needs to have at least 2 characters'
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = 'Not a valid email'
    if len(postData['message']) < 10: 
      errors['message'] = 'Message needs to have at least 10 characters'
    
    return errors

# Message model
class  Message(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=200)
  message = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = MessageManager()

  def __str__(self):
    return f'{self.name}'
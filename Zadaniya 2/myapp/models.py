from django.db import models
from myapp.general.models import BaseModel

# Create your models here.

class MessageModel(BaseModel):
    name = models.CharField(max_length=36)
    email = models.CharField(max_length=36)
    subject = models.CharField(max_length=36)
    text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.name}--{self.email}--{self.text}"
    
class Testimonial(BaseModel):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}: write {self.description}"
    
class TeamModel(BaseModel):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}"
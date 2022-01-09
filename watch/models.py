from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

Priority=(
    ('Informational', 'Informational'),
    ('High Priority', 'High Priority'),
)
# Create your models here.
# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, neighbourhood_name):
        cls.objects.filter(neighbourhood_name=neighbourhood_name).delete()

    @classmethod
    def find_neighbourhood(cls, search_term):
        search_results = cls.objects.filter(neighbourhood_name__icontains = search_term)
        return search_results

    def update_neighbourhood(self, neighbourhood_name):
        self.neighbourhood_name = neighbourhood_name
        self.save()
        
class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15, choices=Priority, default="Informational")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE
    )
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls, healthservices):
        cls.objects.filter(healthservices=healthservices).delete()

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name
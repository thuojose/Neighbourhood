from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

Priority=(
    ('Informational', 'Informational'),
    ('High Priority', 'High Priority'),
)
# Create your models here.
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

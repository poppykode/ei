from django.db import models
from accounts.models import User

# Create your models here.

class Thing(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank =True, height_field='height_field', width_field='width_field' )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    
    def  __str__(self): 
        return self.title

    class Meta:
        ordering = ["-timestamp",]


from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')



class Project(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)     
    developer=models.CharField(max_length=300)
    created_date=models.DateField()
    averangeRating=models.FloatField(default=0)
    image=models.URLField(default=None, null=True)
    linktosite=models.URLField(default=None, null=True)
   


    def __str__(self):
        return self.name

    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(name__icontains = search)
        return searches


RATE_CHOICES = [

    (1, '1 - very poor'),
    (2, '2 - poor'),
    (3, '3 - Terrible'),
    (4, '4 -good'),
    (5, '5 -very good'),
    (6, '6 -perfect'),
    (7, '7 -Exellent'),
    (8, '8-world class'),



]


class Review(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    project = models.ForeignKey(Project, models.CASCADE)
    text = models.CharField(max_length=200,blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    



    def __str__(self):
        return self.user.username

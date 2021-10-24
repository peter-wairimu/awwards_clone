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


class Review(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    project = models.ForeignKey(Project, models.CASCADE)
    comment = models.TextField(max_length=500)
    rate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

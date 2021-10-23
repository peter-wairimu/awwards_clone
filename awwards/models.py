from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')



class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='pro_image')
    description = models.TextField(max_length=600, blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boards(models.Model):
    name = models.CharField(max_length=50,unique=True,default=True)
    descreption = models.CharField(max_length=250,default=False)
    def __str__(self):
        return self.name
class Topics(models.Model):
    name = models.CharField(max_length=50,unique=True,default=False)
    board = models.ForeignKey(Boards,related_name='topic',on_delete=models.CASCADE,default=True)
    creata_by = models.ForeignKey(User,related_name='topic',on_delete=models.CASCADE,default=True)
    #creat_date : models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    message = models.CharField(max_length=4000,default=True)
    topic = models.ForeignKey(Topics,related_name='posts',on_delete=models.CASCADE,default=False)
    posted_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,default=True)
   # posted_by = models.On(User,related_name = "posts",on_delete=models.CASCADE,default=True)
   # creat_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
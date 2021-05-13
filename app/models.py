from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile_owner")
    age = models.IntegerField(default=0)
    major = models.CharField(max_length=50)
    prog_langs = models.CharField(max_length=300)
    comment = models.TextField(max_length=300)

    def __str__(self):
        txt = "<UserID:"+str(self.id)+"| Name:"+str(self.owner.first_name)+" "+str(self.owner.last_name)+"| Age:"+str(self.age)+">"
        return txt

class Friend(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friend_owner")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        txt = "<"+str(self.owner.first_name)+" -> "+str(self.user.first_name)+">"
        return txt

class Image(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="image_owner")
    image = models.ImageField(upload_to="img")

    def __str__(self):
        txt = "<"+str(self.image)+">"
        return txt
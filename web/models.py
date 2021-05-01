from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class ProfileImg(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    profileimg = VersatileImageField(upload_to='profile',default='prifiledummy.png')


    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=1000,null=True)
    detailDiscription = RichTextUploadingField(blank=True,null=True)
    place =  models.CharField(max_length=300,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cover_image = VersatileImageField(upload_to='web',default='default.jpg')
    twoimage = VersatileImageField(upload_to='web',default='default.jpg')
    threeimage = VersatileImageField(upload_to='web',default='default.jpg')



    def __str__(self):
        return self.title
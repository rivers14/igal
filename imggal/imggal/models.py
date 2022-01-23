from django.db import models

class imgggal(models.Model):
    imgtitle=models.CharField(max_length=100)
    imgdesc=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/')

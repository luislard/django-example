from django.db import models

# Create your models here.
class Blog(models.Model):
   titulo = models.CharField(max_length=150)
   subtitulo = models.CharField(max_length=150)
   cuerpo = models.TextField(blank=True,default="", null=True)
   fecha = models.DateTimeField()
   author = models.CharField(max_length=150)
   imagen = models.ImageField(upload_to="uploads/%Y/%m/%d/")
   created_at = models.DateTimeField(auto_now_add=True)
   modified_at = models.DateTimeField(auto_now=True)
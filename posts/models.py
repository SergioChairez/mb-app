from django.db import models

# Create your models here.

class Post(models.Model):
  texto = models.TextField()

  def __str__(self):
    return self.texto[:50]
from django.db import models

# Create your models here.

class Skill(models.Model):
    title = models.CharField(max_length = 255)

class Message(models.Model):
    name = models.CharField(max_length= 255, verbose_name= 'Введите ваше имя')
    email = models.EmailField(verbose_name= 'Введите электронную почту')
    text = models.TextField(verbose_name= 'Сообщение')

class Project(models.Model):
    title = models.CharField(max_length = 255)
    discription = models.TextField()
    link = models.TextField()
    image = models.ImageField(upload_to='static')

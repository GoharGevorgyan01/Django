from django.db import models

# Create your models here.

class Home(models.Model):
    name1 = models.CharField('Home name1',max_length=100)
    name2 = models.CharField('Home name2',max_length=100)
    about = models.TextField('Home About',max_length=500)
    img = models.ImageField('Home Image',upload_to='Photo')

    def __str__(self) -> str:
        return self.name1

class Base(models.Model):
    logoo = models.ImageField('Logo',upload_to='Photo')
    title = models.CharField('Title page',max_length=100)
    foot = models.CharField('Footer',max_length=50)

    def __str__(self) -> str:
        return self.title
    
class About(models.Model):
    name1 = models.CharField('About name1',max_length=100)
    name2 = models.CharField('About name2',max_length=100)
    about = models.TextField('About Us',max_length=500)
    img = models.ImageField('About Image',upload_to='Photo')
    
    def __str__(self) -> str:
        return self.name2

class Project(models.Model):
    img = models.ImageField('Project Image',upload_to='Photo')
    name = models.CharField('About name',max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    name = models.CharField('name',max_length=50)
    message = models.TextField('message',max_length=500)
    email = models.EmailField('email')

    def __str__(self) -> str:
        return self.name
    
class ContactAbout(models.Model):
    about1 = models.TextField('Contact About1',max_length=500)
    about2 = models.TextField('Contact About2',max_length=500)
    adress1 = models.CharField('Adress1',max_length=50)
    adress2 = models.CharField('Adress2',max_length=50)

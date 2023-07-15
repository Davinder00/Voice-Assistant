from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

  

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title
    

class Writer(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    

class Genre(models.Model):
    type=models.CharField(max_length=200)
    details = models.TextField()


    def __str__(self):
        return self.type


class About_us(models.Model):
    about = models.TextField()



class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    
    def __str__(self):
        return self.name
    

class Topseller(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    





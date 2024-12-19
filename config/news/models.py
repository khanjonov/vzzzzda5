from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150,unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="courses/phots/",blank=True,null=True)
    def __str__(self):
        return self.title
    
    
    
class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    enrolled_at = models.DateTimeField(auto_created=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
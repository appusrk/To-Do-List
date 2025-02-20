from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    ontime=models.TimeField(null=True)

    def __str__(self):
        return self.title
    
class Reg(models.Model):
    name=models.CharField(max_length=200)
    passw=models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

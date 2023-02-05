from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    
    
    def __str__(self):
        return"%s %s" %(self.name,self.email)
    
    

# Create your models here.


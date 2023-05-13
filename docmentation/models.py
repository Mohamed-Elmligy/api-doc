from django.db import models

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

api_methods = [
('GET', 'Get'),
('POST', 'Post'),
('PUT', 'Put'),
('DELETE', 'Delete')
] 

class Api (models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    header = models.BooleanField(default=False)
    method = models.CharField(max_length=10 , choices=api_methods, default='GET') 
    project = models.ForeignKey(Project, related_name='apis', on_delete=models.CASCADE)  
    def __str__(self):
        return self.name
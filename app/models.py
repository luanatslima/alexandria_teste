from django.db import models

class Usuario(models.Model): 
    email = models.EmailField() 
    senha = models.CharField(max_length=11) 
    
    def __str__(self): 
        return self.email
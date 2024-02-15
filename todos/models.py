from django.db import models

# Model class 
class Todo(models.Model):  #inherit class from namespace models 
    content = models.TextField()
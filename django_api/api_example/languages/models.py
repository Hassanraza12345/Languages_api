from django.db import models

# Create your models here.


class Languages(models.Model):
    name=models.CharField(max_length=50)
    paradigm=models.CharField(max_length=50)
    # the code up to here only return the object of the languages like Language_object1,2 and so on to 
    # show the language name 

    def __str__(self):
        return self.name
    

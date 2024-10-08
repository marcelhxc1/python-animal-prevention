from django.db import models

# Create your models here.

class Sighting(models.Model):
    cep = models.CharField(max_length=9)
    animal_type = models.CharField(max_length=100)
    date = models.DateField()
    action_taken = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal_type} sighting on {self.date} at {self.cep}"



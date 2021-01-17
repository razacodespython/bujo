from django.db import models

# Create your models here.

class bujodb(models.Model):
    DAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
        ('X', 'Otherstuff'),
        
    )

    day = models.CharField(max_length=2, choices=DAYS, default='X')


    text = models.TextField()

def __str__(self):
    return self.day

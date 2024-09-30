from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    data_pubblicazione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titolo


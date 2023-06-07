from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.FloatField(default=0.0)
    categories = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Article(models.Model):
    Author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Surname = models.CharField(max_length=100)
    Age = models.IntegerField()
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Created_time = models.DateTimeField( auto_now_add=True)

    def __str__(self):  
         return f"{self.Title} "
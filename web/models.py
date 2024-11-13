from django.db import models

# Create your models here.
class Notification(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/")
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField() 
    playlist_url = models.URLField(blank=True, null=True, help_text="Enter the URL for a YouTube playlist.")
    chapter_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title # same like models.URLField()

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    class_name = models.CharField(max_length=50)  # Consider renaming if 'class' conflicts with Python keywords
    mode_of_class = models.CharField(max_length=50, choices=[('Online', 'Online'), ('Offline', 'Offline')])
    class_timings = models.CharField(max_length=100)  # You may use DateTimeField if specific times are needed
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='class_images/')

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	video_link = models.URLField(blank=True)
	video_file = models.FileField(upload_to='videos/', blank=True)

	def __str__(self):
		return self.title


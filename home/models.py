from django.db import models

# Create your models here.

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	message = models.TextField()
	received_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s - %s" % (self.email, self.received_date)



class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	image = models.ImageField(upload_to="blog", null=True, blank=True)
	date = models.DateField()
	url=models.CharField(max_length=300)

	def __strt__(self):

		return self.title


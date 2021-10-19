from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

class Tag(models.Model):
	name = models.CharField(max_length=100)

class Product(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	affiliate_link = models.TextField()

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)

	views = models.IntegerField(default=0)

class Blog(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)

	views = models.IntegerField(default=0)

class Email(models.Model):
	email = models.CharField(primary_key=True, max_length=100)
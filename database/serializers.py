from rest_framework import serializers
from . import models

class Category_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = models.Category
		fields = ("name", )

class Tag_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = models.Tag
		fields = ("name", )

class Product_Serializer(serializers.ModelSerializer):
	category = Category_Serializer(many=False)
	tags = Category_Serializer(many=True)
	class Meta(object):
		model = models.Product
		exclude = ("views", )

class Blog_Serializer(serializers.ModelSerializer):
	category = Category_Serializer(many=False)
	tags = Category_Serializer(many=True)
	class Meta(object):
		model = models.Blog
		exclude = ("views", )

class Email_Serializer(serializers.ModelSerializer):
	class Meta(object):
		model = models.Email
		fields = ("email", )
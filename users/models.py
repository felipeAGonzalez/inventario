from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
	name = models.CharField(max_length=200)
	search = models.CharField(max_length=600)
	last_name_1 = models.CharField(max_length=200)
	last_name_2 = models.CharField(max_length=200,null=True)
	email = models.EmailField(max_length = 254, unique=True)
	password = models.CharField(max_length=255)
	preferred_language = models.CharField(max_length=5,default='es')
	deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	username = None
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

class Meta:
	ordering = ["-id"]
	db_table = 'user'
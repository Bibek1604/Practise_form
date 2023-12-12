from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages




class Contact(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=33, null=False, blank=False)
    phn = models.CharField(max_length=15, null=False, blank=False)
    message = models.TextField(null=False, blank=False, default='')  # Default value added ('' in this case)


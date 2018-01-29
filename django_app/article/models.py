#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    summary = models.TextField(blank=True, null=True)
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField()
    video = models.FileField(upload_to='article')
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class FileNode(models.Model):
    isDir = models.BooleanField(default=False)
    name = models.FileField(max_length=30)
    file = models.FileField(upload_to="share")
    parent = models.ForeignKey("self", related_name='dir', null=True)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Temperature(models.Model):
	tem_value=models.CharField(max_length=250)
	hum_value=models.CharField(max_length=250)
        soil_value=models.CharField(max_length=250)

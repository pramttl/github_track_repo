from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.Register(models.Project)
admin.site.Register(models.DataPoint)

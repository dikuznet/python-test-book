from django.db import models

# Create your models here.
class Demo(models.Model):

    class Meta:
        db_table = "demo"
        
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Employee_Benefits(models.Model):
    benefits = RichTextField(verbose_name="Benefits")

    def __str__(self):
        return "Employee-Benefits"

    class Meta:
        verbose_name = "Employee Benefit"
        verbose_name_plural = "Employee Benefits"

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


class Job_Opening(models.Model):
    job_title = models.CharField(
        max_length=225, blank=False, null=False, verbose_name="Job Title")
    job_description = RichTextField(verbose_name="Job Description")

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "Job Opening"


class Areas(models.Model):
    areas = RichTextField(verbose_name="Areas With Their Services")

    def __str__(self):
        return "Areas"

    class Meta:
        verbose_name = "Areas & Service"

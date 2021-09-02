from typing import Iterable
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.expressions import F
from django.utils.text import slugify
from django.urls import reverse

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
        verbose_name_plural = "Areas & Services"


class Branch(models.Model):
    branch_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Branch Name")
    slug = models.SlugField(unique=True,default="null")
    branch_address = models.CharField(
        max_length=20000, null=False, blank=False, verbose_name="Embeded Google Map Link")
    phone = models.CharField(max_length=13, blank=False,
                             null=False, verbose_name="Phone Number")
    fax = models.CharField(max_length=15, blank=True,
                           null=True, verbose_name="Fax")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    team_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.branch_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.branch_name)
        super(Branch, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('branch_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Team(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name="Name of Employee")
    image = models.ImageField(upload_to="team/", blank=False, null=False)
    branch = models.ForeignKey(
        Branch, related_name="branch", on_delete=models.CASCADE, verbose_name="Branch")
    designation = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Designation of Employee")
    working_on = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Working in Row")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

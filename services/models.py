from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
# Create your models here.


class Nursing_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/skilled-nursing', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Skilled Nurse Service"

    class Meta:
        verbose_name = "Skilled Nurse (SN) Service"
        verbose_name_plural = "Skilled Nurse (SN)"


class Care_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/home-care-nursing', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Home Care Nursing Service"

    class Meta:
        verbose_name = "Home Care Nursing (HCN) Service"
        verbose_name_plural = "Home Care Nursing (HCN)"


class Aid_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/home-health-aide', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Health Aide Service"

    class Meta:
        verbose_name = "Home Health Aide Service"
        verbose_name_plural = "Home Health Aide"


class Assistant_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/perosonal-care', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Personal Care Assistant Service"

    class Meta:
        verbose_name = "Personal Care Assistance (PCA) Service"
        verbose_name_plural = "Personal Care Assistance (PCA)"


class Homemaking_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/homemaking-service', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Homemaking Service"

    class Meta:
        verbose_name = "Homemaking Services Service"
        verbose_name_plural = "Homemaking Services"


class Therapy_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/therapy', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Therapy Service"

    class Meta:
        verbose_name = "Therapy Service"
        verbose_name_plural = "Therapy"


class IV_Therapy_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/iv-therapy', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " IV Therapy Service"

    class Meta:
        verbose_name = "IV Therapy Service"
        verbose_name_plural = "IV Therapy"


class Interpretive_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/interpretive', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Interpretive Service"

    class Meta:
        verbose_name = "Interpretive Services Service"
        verbose_name_plural = "Interpretive Services"


class Living_Skills_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/independent-living', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Indp Living Skills Service"

    class Meta:
        verbose_name = "Independent Living Skills (ILS) Service"
        verbose_name_plural = "Independent Living Skills (ILS)"


class Companion_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/companion', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Companion Service"

    class Meta:
        verbose_name = "Companion Service"
        verbose_name_plural = "Companion"


class Respite_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/respite', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Respite Service"

    class Meta:
        verbose_name = "Respite Service"
        verbose_name_plural = "Respite"


class Social_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/social-service', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Social Service"

    class Meta:
        verbose_name = "Social Services Service"
        verbose_name_plural = "Social Services"


class Hospice_Service(models.Model):
    service_name = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Heading")
    service_image = models.ImageField(
        upload_to='service_uploads/hospice', blank=True, null=True, verbose_name="Image")
    blog = RichTextField(verbose_name="Details of Service")

    def __str__(self):
        return self.service_name + " Hospice Service"

    class Meta:
        verbose_name = "Hospice Service"
        verbose_name_plural = "Hospice"

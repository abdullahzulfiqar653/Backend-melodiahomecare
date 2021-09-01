from django.db import models

# Create your models here.


class Hospice(models.Model):
    question = models.CharField(
        max_length=1000, blank=False, null=False, verbose_name="Question")
    image = models.ImageField(
        upload_to="Hospice", blank=True, null=True, verbose_name="Image")
    description = models.TextField(
        blank=False, null=False, verbose_name="Answer")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "What is Hospice?"
        verbose_name_plural = "What is Hospice?"


class FAQ(models.Model):
    question = models.CharField(
        max_length=1000, blank=False, null=False, verbose_name="Question")

    description = models.TextField(
        blank=False, null=False, verbose_name="Answer")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

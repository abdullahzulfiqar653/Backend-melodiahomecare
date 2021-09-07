from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="First Name")
    last_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Last Name")
    address = models.CharField(
        max_length=1024, null=False, blank=False, verbose_name="Address")
    city = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name="City")
    state = models.CharField(max_length=255, null=False,
                             blank=False, verbose_name="State")
    zip_code = models.CharField(
        max_length=6, null=False, blank=False, verbose_name="Zip Code")
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=False,
                             null=False, verbose_name="Phone Number")
    questions = models.TextField(
        null=False, blank=False, verbose_name="Comments/Questions")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.expressions import F
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Employee_Benefits(models.Model):
    heading = models.CharField(
        max_length=1024, blank=False, null=False, verbose_name="What Benefit?")
    benefits = RichTextField(verbose_name="Benefits")

    def __str__(self):
        return "Employee-Benefits"

    class Meta:
        verbose_name = "Employee Benefit"
        verbose_name_plural = "Employee Benefits"


class Job_Opening(models.Model):
    job_title = models.CharField(
        max_length=225, blank=False, null=False, verbose_name="Job Title")
    job_description = RichTextField(verbose_name="Job Description and Areas")

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
    slug = models.SlugField(unique=True, default="null")
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


class Apply_Now(models.Model):
    FIRST_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('does-not-apply', 'Does Not Apply')
    ]
    SECOND_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    ABOUT_CHOICES = [
        ('radio', 'Radio'),
        ('friends', 'Friend'),
        ('website', 'Website'),
        ('ads', 'ADS'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('others', 'Others')
    ]
    application_date = models.DateField(
        null=False, blank=False, verbose_name="Date of Application")
    position = models.CharField(
        max_length=10, null=False, blank=False, verbose_name="Position(s) Applied For")
    location = models.ForeignKey(Branch, related_name="location",
                                 on_delete=models.CASCADE, verbose_name="Branch applying for")
    about = models.CharField(max_length=255, null=False, blank=False,
                             verbose_name="How did you hear about us?", choices=ABOUT_CHOICES)
    reffer = models.CharField(max_length=255, blank=False, null=False,
                              verbose_name="If reffered by other employ please enter the name below.")
    under_18 = models.CharField(max_length=15, blank=False, null=False,
                                verbose_name="If you are under 18 can you provide proof of your eligibility of work?", choices=FIRST_CHOICES)
    other_company_work = models.CharField(
        max_length=5, blank=False, null=False, verbose_name="Hove you worked for our company?", choices=SECOND_CHOICES)
    employeed = models.CharField(max_length=5, blank=False, null=False,
                                 verbose_name="Are you currently Employed?", choices=SECOND_CHOICES)
    first_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="First Name")
    last_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Last Name")
    address1 = models.CharField(
        max_length=1024, null=False, blank=False, verbose_name="Address 1")
    address2 = models.CharField(
        max_length=1024, null=True, blank=True, verbose_name="Address 2", default="null")
    city = models.CharField(max_length=255, null=False,
                            blank=False, verbose_name="City")
    state = models.CharField(max_length=255, null=False,
                             blank=False, verbose_name="State")
    zip_code = models.CharField(
        max_length=6, null=False, blank=False, verbose_name="Zip Code")
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    phone = models.CharField(max_length=25, blank=False,
                             null=False, verbose_name="Phone Number")
    available = models.DateField(
        blank=False, null=False, verbose_name="On what date could you be avilable for work?")
    travel = models.CharField(max_length=15, blank=False, null=False,
                              verbose_name="Can you travel if your job requires it?", choices=SECOND_CHOICES)
    cv = models.FileField(upload_to="Application-forms/cv/", verbose_name="CV")
    signature = models.FileField(
        upload_to="Application-forms/signature/", verbose_name="Digital Signature")

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + self.city + " - "+self.state

    class Meta:
        verbose_name = "Application Form"
        verbose_name_plural = "Application Forms"

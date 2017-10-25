from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(datetime.datetime.now().year, (datetime.datetime.now().year+10)):
    YEAR_CHOICES.append((r, r))


# Create your models here.
# This is Our Database model for profile System
class Member(models.Model):
    profilePic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=100)
    University = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=100)
    collegeDepartment = models.CharField(max_length=50)
    collegeID = models.CharField(max_length=11)
    graduationYear = models.IntegerField(max_length=4, choices=YEAR_CHOICES)
    parent1 = models.CharField(max_length=50)
    parent1Mobile = models.CharField(max_length=11)
    parent2 = models.CharField(max_length=50, blank=True)
    parent2Mobile = models.CharField(max_length=11, blank=True)
    nationalID = models.CharField(max_length=14)
    passportID = models.CharField(max_length=14, blank=True)
    drivingID = models.CharField(max_length=14, blank=True)
    haveCar = models.BooleanField()
    Weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.firstName

from django.db import models


# Create your models here.
#This is Our Database model for profile System
class ASUmember(models.Model):
	profilePic = models.CharField(max_length=30)
	firstName = models.CharField(max_length=50, null=False)
	middleName = models.CharField(max_length=50, null=False)
	lastName = models.CharField(max_length=50, null=False)
	Mobile = models.CharField(max_length=12)
	email = models.CharField(max_length=50)
	Address=models.CharField(max_length=100)
	University=models.CharField(max_length=50)
	Faculty=models.CharField(max_length=100)
	collegeDepartment=models.CharField(max_length=50)
	collegeID=models.CharField(max_length=8)
	graduationYear=models.CharField(max_length=4)
	parent1=models.CharField(max_length=50)
	parent1Mobile = models.CharField(max_length=12)
	parent2=models.CharField(max_length=50,null=True)
	parent2Mobile = models.CharField(max_length=12,null=True)
	nationalID=models.CharField(max_length=14)
	passportID=models.CharField(max_length=14,null=True)
	drivingID=models.CharField(max_length=14,null=True)
	haveCar=models.BooleanField()
	Weight =models.IntegerField()
	Height =models.IntegerField()
	def __str__(self):
		return self.firstName


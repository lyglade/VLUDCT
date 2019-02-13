from django.db import models

# Create your models here.
class HSS_Data(models.Model):
    HSS = models.CharField(max_length=30)
    MSISDN=models.CharField(max_length=20)
    IMPI=models.CharField(max_length=50)
    IMPU=models.CharField(max_length=255)
    YHDZD_number=models.CharField(max_length=20)


class ENUM_DNS(models.Model):
    MSISDN=models.CharField(max_length=20)
    IMPI=models.CharField(max_length=50)
    
class AS_Data(models.Model):
    MSISDN=models.CharField(max_length=20)
    IMPI=models.CharField(max_length=50)
    
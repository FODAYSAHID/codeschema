from django.db import models

# Create your models here.

class Computer(models.Model):
	staff_or_office = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	pc_model = models.CharField(max_length=20)
	IP_Address = models.CharField(max_length=30)
	MAC_Address = models.CharField(max_length=30)
	serial_number = models.CharField(max_length=30, default='None')
	ups = models.CharField(max_length=3, default='No')
	condition = models.CharField(max_length=10, default='Working')
	network_connection = models.CharField(max_length=30, default='None')
	no_of_network_field = models.CharField(max_length=10, default='None')

class Printer(models.Model):
    staff_or_office = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    printer_or_copier_model = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=40)
    shared = models.CharField(max_length=3)
    condition = models.CharField(max_length=10)
    toner = models.CharField(max_length=30)

class Wireless_Connection(models.Model):
    staff_or_office = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    connection_model = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=40)
    condition = models.CharField(max_length=10)  
 
    def __unicode__(self):
       return self.computer_name

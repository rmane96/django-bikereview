from djongo import models


class Bike(models.Model):
    id = models.AutoField(primary_key=True)
    
    TVS = 'TVS'
    BAJAJ = 'BAJAJ'
    YAMAHA = 'YAMAHA'
    HERO = 'HERO'
    HONDA = 'HONDA'
    
    BRAND_CHOICES = [
        (TVS, 'TVS'),
        (BAJAJ, 'BAJAJ'),
        (YAMAHA, 'YAMAHA'),
        (HERO, 'HERO'),
        (HONDA, 'HONDA'),
    ]
    
    brand = models.CharField(max_length=15, choices=BRAND_CHOICES, blank=False)
    
    model = models.CharField(max_length=30,blank=False)
    capacity = models.IntegerField(blank=False)
    weight = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    mileage = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    
    
    PETROL = 'PETROL'
    DIESEL = 'DIESEL'
    ELECTRIC = 'ELECTRIC'
    
    FUEL_TYPE = [
        (PETROL,'PETROL'),
        (DIESEL,'DIESEL'),
        (ELECTRIC,'ELECTRIC'),
    ]
    fuel_type = models.CharField(max_length=10,choices=FUEL_TYPE,blank=False)

    
    DRUM_BRAKE = 'Drum Brake'
    DISK_BRAKE = 'Disk Brake'
    BRAKES = [
            (DRUM_BRAKE,'Drum Brake'),
            (DISK_BRAKE,'Disk Brake'),
    ]
    brakes = models.CharField(max_length=25,choices=BRAKES,blank=False) 
    
    SINGLE_CHANNEL = 'Single Channel'
    DUAL_CHANNEL = 'Dual Channel'
    
    ABS_TYPE = [
        (SINGLE_CHANNEL,'Single Channel'),
        (DUAL_CHANNEL,'Dual Channel')
    ]
    abs = models.CharField(max_length=20,choices=ABS_TYPE,default='NA')
    
    description = models.TextField(max_length=50,blank=True)
    price = models.IntegerField(blank=False)
    
    image = models.FileField(upload_to='images/')
from djongo import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Bike(models.Model):
    id = models.AutoField(primary_key=True)
    
    TVS = 'TVS'
    BAJAJ = 'Bajaj'
    YAMAHA = 'Yamaha'
    HERO = 'Hero'
    HONDA = 'Honda'
    
    BRAND_CHOICES = [
        (TVS, 'TVS'),
        (BAJAJ, 'Bajaj'),
        (YAMAHA, 'Yamaha'),
        (HERO, 'Hero'),
        (HONDA, 'Honda'),
    ]
    
    brand = models.CharField(max_length=15, choices=BRAND_CHOICES, blank=False)
    
    model = models.CharField(max_length=30,blank=False)
    capacity = models.IntegerField(blank=False)
    weight = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    mileage = models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    
    PETROL = 'Petrol'
    ELECTRIC = 'Electric'
    
    FUEL_TYPE = [
        (PETROL,'Petrol'),
        (ELECTRIC,'Electric'),
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
    NA = 'NA'
    
    ABS_TYPE = [
        (SINGLE_CHANNEL,'Single Channel'),
        (DUAL_CHANNEL,'Dual Channel'),
        (NA,'NA'),
    ]
    abs = models.CharField(max_length=20,choices=ABS_TYPE,default='NA')
    
    description = models.TextField(max_length=50,blank=True)
    price = models.IntegerField(blank=False)
    
    image = models.FileField(upload_to='images/')
    
    

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='reviews')
    
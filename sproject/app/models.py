from django.db import models

# Create your models here.

class Player(models.Model):
    player_Teamname = models.CharField(max_length=80, unique= True)
    address = models.TextField(blank=True, null=True)
    contactnumber = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.player_Teamname)

class Employee(models.Model):
    employee_name = models.CharField(max_length=80, unique= True)
    address = models.TextField(blank=True, null=True)
    citizenshipnumber= models.TextField(blank=True, null=True)
    contactnumber = models.TextField(blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.employee_name)

class Booking(models.Model):
    booker_name = models.CharField(max_length=80,unique=True)
    start_time = models.TextField(blank=True, null=True)
    end_time = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    contactnumber = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.booker_name)

    

class Match(models.Model):
    start_time = models.TextField(blank=True, unique= True)
    end_time = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.start_time)

class Payment(models.Model):
    status = models.CharField(max_length=100, unique= True)   
    amount = models.TextField(blank=True, null=True) 
    method= models.TextField(blank=True, null=True)
    Teamname = models.CharField(max_length=80,default=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)


    match = models.OneToOneField(Match,on_delete=models.PROTECT,null=True,blank=True)
    player = models.ForeignKey(Player,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return str(self.status)

class Price(models.Model):
    start_time = models.TextField(blank=True, unique= True)
    price = models.IntegerField(default=True)
    end_time = models.TextField(blank=True, null=True)
    day = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.start_time)

    
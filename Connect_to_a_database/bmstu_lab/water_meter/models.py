from django.db import models


class Addresses(models.Model):
    address_id = models.IntegerField(primary_key=True)
    town = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    apartment = models.IntegerField()
    house_type = models.CharField(max_length=12)
    images = models.ImageField(blank=True, null=True)
    meter_reading = models.IntegerField()
    address_status = models.CharField(max_length=12)
    
    class Meta:
        managed = False
        db_table = 'addresses'


class ManyToMany(models.Model):
    many_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    water_meter_reading = models.ForeignKey('WaterMeterReading', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'many_to_many'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WaterMeterReading(models.Model):
    water_meter_reading_id = models.IntegerField(primary_key=True)
    create_date = models.DateField()
    fixation_date = models.DateField()
    finish_date = models.DateField()
    full_name_creater = models.CharField(max_length=50)
    meter_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'water_meter_reading'
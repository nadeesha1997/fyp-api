from django.db import models


# class Question(models.Model):
#     pub_date = models.DateTimeField('date published')
#     user_id = models.CharField(max_length=20)

class Value(models.Model):
    val1 = models.IntegerField(default=0)
    val2 = models.IntegerField(default=0)
    val3 = models.IntegerField(default=0)

    def __str__(self):
        return self.value_text

class Sensor(models.Model):
    sensor_id = models.CharField(max_length=20)
    values = models.ManyToManyField(Value)

    def __str__(self):
        return self.sensor_tetxt

class Device(models.Model):
    device_id = models.CharField(max_length=20)
    sensors=models.ManyToManyField(Sensor)

    def __str__(self):
        return self.device_text

class Reading(models.Model):
    reading_id = models.CharField(max_length=20)
    devices=models.ManyToManyField(Device)

    def __str__(self):
        return self.reading_text




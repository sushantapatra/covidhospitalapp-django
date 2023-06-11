from django.db import models

# Create your models here.

# create a  Schema for state table


class State(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)

    # Formating models object to show human readable
    def __str__(self):
        return self.name


# create a  Schema for city table
class City(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='cities')  # state.cities

    # Formating models object to show human readable
    def __str__(self):
        return self.name


# create a  Schema for hospital table
class Hospital(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='hospitals')  # city.hospitals

    # Formating models object to show human readable
    def __str__(self):
        return self.name


# create a  Schema for Facility table
class Facility(models.Model):
    title = models.CharField(
        max_length=60, null=False, blank=False, default='')

    # Formating models object to show human readable
    def __str__(self):
        return self.title


# create a  Schema for Availability table
class Availability(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="availabilities")
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, related_name="availabilities")
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    # Formating models object to show human readable
    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'

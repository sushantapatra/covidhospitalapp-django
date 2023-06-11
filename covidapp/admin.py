from django.contrib import admin

from covidapp.models import State, City, Hospital, Facility, Availability


# use signals for save an hospital in that time send a signal to save services
from django.db.models.signals import post_save
from django.dispatch import receiver


# after save data on hospital table automatically send a signal to store data on availbility table
@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    # print('Save services for ', instance.name, signal, kwargs)
    facilities = Facility.objects.all()
    for facility in facilities:
        availbilityObj = Availability(hospital=instance, facility=facility)
        availbilityObj.save()


# after save data on facility table automatically send a signal to store data on availbility table
@receiver(post_save, sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
    # print('Save services for ', instance.name, signal, kwargs)
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
        availbility = Availability(hospital=hospital, facility=instance)
        availbility.save()


# Show availability table data in a table format
class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    # list_display main pass kiya gaya har attribute/property ko table se find karega nehi mila to as a function search karega
    list_display = ['hospital', 'facility', 'total', 'available', 'updated_at']
    # Editable format on by table list
    list_editable = ['total', 'available']


# Show facility table data in a table format
class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    # list_display main pass kiya gaya har attribute/property ko table se find karega nehi mila to as a function search karega
    list_display = ['title',]

# Show hospital table data in a table format


class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    # list_display main pass kiya gaya har attribute/property ko table se find karega nehi mila to as a function search karega
    list_display = ['name', 'phone', 'address', 'city',]

# Show city table data in a table format


class CityAdmin(admin.ModelAdmin):
    model = Hospital
    # list_display main pass kiya gaya har attribute/property ko table se find karega nehi mila to as a function search karega
    list_display = ['name', 'state',]


# Register your models here. it's effected on admin login
admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availability, AvailabilityAdmin)

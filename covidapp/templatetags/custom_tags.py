from django import template
from covidapp.models import Availability

# register to template library
register = template.Library()


# create a custom helper file to impliment in html page
@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'

    return 'bg-danger'


# create a custom helper file to implimenting in html page
@register.simple_tag
def get_availabilities(hospital):
    # get all availability data filter by hospital and order by ficilty primery key
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


# form select box option selected function
@register.simple_tag
def is_selected(selected_id, id):
    if selected_id != "":
        if int(selected_id) == id:
            return 'selected'
        return ''
    return ''

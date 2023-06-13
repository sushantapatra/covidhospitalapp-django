from django.shortcuts import render
from django.http.response import HttpResponse
from covidapp.models import Facility, State, City, Hospital, Availability

from django.views import generic

# Create your views here.

"""Create a Hospial Details page class base view"""


class HospitalDetailView(generic.DetailView):
    model = Hospital


"""Create a Home page function base view"""


def home(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')

    # get all facility order by title
    facilities = Facility.objects.all().order_by(
        'pk')
    if selected_state_id:
        cities = City.objects.filter(state=selected_state_id)  # Get all cities
    else:
        cities = City.objects.all()  # Get all cities

    states = State.objects.all()  # Get all States
    if selected_city_id:
        hospitals = Hospital.objects.filter(
            city=selected_city_id)  # Get all hospital
    else:
        hospitals = Hospital.objects.all()  # Get all hospital

    if selected_facility_id:
        if selected_city_id:
            # get all availities filter by hospital field(foreign key) se city and facility id se
            availities = Availability.objects.filter(hospital__city=City(pk=selected_city_id), facility=Facility(
                pk=selected_facility_id), available__gt=0)
        else:
            availities = Availability.objects.filter(facility=Facility(
                pk=selected_facility_id), available__gt=0)  # get all facility order by title

        hospitals = []
        for avl in availities:
            hospitals.append(avl.hospital)

    else:
        availities = Availability.objects.filter()  # get all facility order by title

    # all data added in context to pass html file
    context = {
        'facilities': facilities,
        'hospitals': hospitals,
        'cities': cities,
        'states': states,
        'selected_state_id': selected_state_id,
        'selected_city_id': selected_city_id,
        'selected_facility_id': selected_facility_id,
    }
    return render(request, template_name="covidapp/index.html", context=context)

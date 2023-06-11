from django.shortcuts import render
from django.http.response import HttpResponse
from covidapp.models import Facility, State, City, Hospital, Availability

# Create your views here.

"""Create a Home page"""


def home(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')

    facilities = Facility.objects.all().order_by(
        'pk')  # get all facility order by title
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
         facilities = Facility.objects.all().order_by(
        'pk')  # get all facility order by title
    else:
        facilities = Facility.objects.all().order_by(
        'pk')  # get all facility order by title

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

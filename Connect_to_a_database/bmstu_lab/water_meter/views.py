from django.db.models import Q
from django.shortcuts import render
from water_meter.models import Addresses
from water_meter.models import WaterMeterReading


def GetApplications(request):
    return render(request, 'applications.html', {'data': Addresses.objects.all()})

def GetApplication(request, address_id):
    address = Addresses.objects.get(address_id=address_id)
    meter_reading = address.meter_reading
    
    return render(request, 'application.html', {'application': address, 'meter_reading': meter_reading})

        
def GetQuery(request):
    query = request.GET.get('query', '')

    # Фильтрация данных из базы данных
    filtered_addresses = Addresses.objects.filter(
        Q(town=query) |
        Q(address=query)
    )

    return render(request, 'applications.html', {'data': filtered_addresses})

def GetMeterReading(request,meter_reading):
    return render(request, 'application.html', {'reading': WaterMeterReading.objects.get(meter_reading=meter_reading)})

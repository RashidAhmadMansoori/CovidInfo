import json
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
import requests

# Covid api
covid_api = "https://api.covid19api.com/summary"


#home page
def home(request):
    if request.method == 'POST':
        location = request.POST['loc']
        return render(request, "home.html", {'loc': location})
    return render(request, "home.html")

#Show page after fetch Covid cases By country
def show(request):
    location = request.GET['loc']
    api_link = requests.get(covid_api)
    api_data = api_link.json()
    # print(api_data)
    for data in api_data["Countries"]:
        if data['Country'].lower() == location.lower():
            country = data['Country']
            totalConfirmedCase = data['TotalConfirmed']
            TotalDeaths = data['TotalDeaths']
            TotalRecovered =data['TotalRecovered']
            date_time = datetime.now().strftime("%d %b %y | %I:%M:%S:%p")
            data = {
                'county':country,
                'totalConfirmedCase':totalConfirmedCase,
                'TotalRecovered':TotalRecovered,
                'TotalDeaths':TotalDeaths,
                'date_time':date_time
            }
            datajson = json.dumps(data)
            return render(request, "home.html", {'data': datajson})

    else:
        print("my name is Rashid")
        messages.warning(request, f"Invailid Country {location.upper()} Please check the Country name")
        return render(request, "home.html")



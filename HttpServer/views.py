from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse, HttpResponse
import datetime
import json
import os.path

# Read a json file
path = os.path.dirname(__file__)
filename = os.path.join(path, 'info.json')
read_data = open(filename)
json_data = json.load(read_data)


# Output application process info
# url: localhost:8000/application/
class ApplicationInfo(APIView):

    def get(self, request):

        # Set and initialize variable
        first_call = ""
        process_time = ""
        current_call = 0
        lifetime_call = 0

        # Check if it is the first time running
        if json_data['FirstCalledDateTime'] == "":
            first_call = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            process_time = "0"
        else:
            first_call = json_data['FirstCalledDateTime']
            process_time = datetime.datetime.now() - json_data['FirstCalledDateTime']
            lifetime_call = json_data['LifetimeTotalCalls']
            current_call = json_data['CurrentTotalCalls']

        # Count the executed time
        current_call += 1
        lifetime_call += 1

        # Update Information to info.json
        info = {
            "ApplicationRunningTime" : process_time,
            "CurrentProcessTotalCalls": current_call,
            "FirstCalledDateTime": first_call,
            "LifetimeTotalCalls": lifetime_call
        }

        # TODO: Overwrite the JSON file

        return JsonResponse(json_data)

    def post(self):

        pass

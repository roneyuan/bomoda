from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import json
import os.path
import atexit

# Read a json file
path = os.path.dirname(__file__)
filename = os.path.join(path, 'info.json')
read_data = open(filename, 'r+')
json_data = json.load(read_data)


# Output application process info
# url: localhost:8000/application/
class ApplicationInfo(APIView):

    def get(self, request):

        # Set and initialize variable
        first_call_ever = ""
        current_process_start_time = ""
        process_time = ""
        current_call = 0
        lifetime_call = 0

        # Check if it is the first time running
        if json_data['FirstCalledDateTime'] == "":
            first_call_ever = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            process_time = "0"

            # Update value to info.json
            json_data["ApplicationRunningTime"] = process_time
            json_data['FirstCalledDateTime'] = first_call_ever
        else:
            # Store current process time to calculate application running time
            if json_data['CurrentProcessStartTime'] == "":
                json_data['CurrentProcessStartTime'] =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            process_time = datetime.now() - datetime.strptime(json_data['CurrentProcessStartTime'], "%Y-%m-%d %H:%M:%S")
            lifetime_call = json_data['LifetimeTotalCalls']
            current_call = json_data['CurrentTotalCalls']
            first_call_ever = json_data['FirstCalledDateTime']

        current_call += 1
        lifetime_call += 1

        # Update the value to the info.json file
        json_data['CurrentTotalCalls'] = current_call
        json_data['LifetimeTotalCalls'] = lifetime_call

        info = {
            "ApplicationRunningTime" : "%s" % process_time,
            "CurrentTotalCalls": current_call,
            "FirstCalledDateTime": first_call_ever,
            "LifetimeTotalCalls": lifetime_call
        }

        # Update info.json file
        read_data.seek(0) # Reset file
        json.dump(json_data, read_data, indent=4)
        read_data.truncate()

        return JsonResponse(info)

    def post(self):

        pass


def handle_exit():
    # Reset Cuurent Call
    current_call = 0
    json_data['CurrentTotalCalls'] = current_call

    # Reset CuurentStartTime
    json_data['CurrentProcessStartTime'] = ""

    # Update info.json file
    read_data.seek(0)  # Reset file
    json.dump(json_data, read_data, indent=4)
    read_data.truncate()


atexit.register(handle_exit)

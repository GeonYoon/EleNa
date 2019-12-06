from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# custom classes
from .algorithm import Navigator
from .models import Model

class PathAPIView(APIView): 

    # As of now, it will give the fake data to the frontend
    def get(self, request, *args, **kwargs):
        
        # 1. Collect the dependencies
        raw_start           = request.GET.get("start", "")          # string
        raw_end             = request.GET.get("end", "")            # string
        threshold           = request.GET.get("threshold", "")      # string
        
        # 2. process them
        start_coordinate    = raw_start.split(",")
        end_coordinate      = raw_end.split(",")

        # DEBUGE PURPOSE
        # start_coordinate = ["42.3818834", "-72.5192702"]
        # end_coordinate = ["42.3681381", "-72.5351446709071"]
    
        # 3. create the objects
        my_model            = Model(start_coordinate,end_coordinate)
        my_navigator        = Navigator(my_model,threshold)

        # 4. run the object
        path, total_travel_distance, total_elevation_gain = my_navigator.get_the_path()

        return Response({"path" :path, "total_travel_distance": total_travel_distance, "total_elevation_gain":total_elevation_gain}, status=200)


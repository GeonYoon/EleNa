from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# install dependencies 
import networkx as nx
import osmnx as ox
from geopy.geocoders import Nominatim


# Create your views here.
fake_data = [ [ -71.0664988, 42.2600685 ],[-71.0665488, 42.2602287],[-71.066564, 42.260285],[ -71.0665737, 42.2603334 ],
[ -71.066576, 42.2603781 ],[ -71.0665728, 42.2604288 ],[ -71.0665624, 42.2604756 ],[ -71.066537, 42.2605203 ],
[ -71.0665028, 42.2605616 ],[ -71.066463, 42.2605995 ],[ -71.066419, 42.2606351 ],[ -71.0663688, 42.2606709 ],
[ -71.0663106, 42.2607083 ],[ -71.0656668, 42.2610566 ],[ -71.0656065, 42.2610933 ],[-71.0655637, 42.2611254 ],
[ -71.0655246, 42.261161 ],[ -71.0654959, 42.2611994 ],[ -71.0654778, 42.2612399 ]]

class PathAPIView(APIView): 

    # As of now, it will give the fake data to the frontend
    def get(self, request, *args, **kwargs):
        data = request.data
        return Response({"start": request.GET.get("start", ""), "end": request.GET.get("end", ""), "threshold": request.GET.get("threshold", ""), "path" : fake_data}, status=200)

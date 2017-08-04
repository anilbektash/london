from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import PlayerSerializer
from .models import Player
from datetime import datetime
import time
from django.http import Http404
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy

class UserList(APIView):
    init_array = numpy.array([[-1, -2, -3]])

    def get(self, request, format=None):
        try:
            user = None
            times = UserList.init_array[:, 2]

            player_id = request.GET["player_id"]
            start = request.GET["start"]
            end = request.GET["end"]
            #First select from the memory
            selected_times = numpy.logical_and(times < int(end), times > int(start))
            indice = 0
            sum = 0
            for i in selected_times:
                if i == True:
                    type = UserList.init_array[indice][1]
                    id = UserList.init_array[indice][0]
                    if id == int(player_id):
                        if type == 1:
                            sum = sum + 1
                        if type == 2:
                            sum = sum + 3
                        if type == 3:
                            sum = sum + 2
                        if type == 4 or type == 5:
                            sum = sum + 5
                indice = indice + 1
            #And then select from the database

            return Response(sum)
        except Exception as ex:
            pass



    def post(self, request, format=None):
        str_time = datetime.strptime(request.data["timestamp"], "%d/%m/%Y %H:%M:%S")
        #--------------_GET POST DATA
        timestamp = int(time.mktime(str_time.timetuple()))
        player_id = int(request.data["player_id"])
        player_type = int(request.data["player_type"])
        # --------------_CONVERT TO OBJECT
        # --------------_IF MEMORY IS LESS THAN (AVAILABLE) 300 MB SAVE TO DB
        # --------------_ELSE SAVE TO NUMPY ARRAY

        UserList.init_array = numpy.vstack((UserList.init_array, [player_id, player_type, timestamp]))

        return redirect('/players/')

    def delete(self, request):
        user = Player.objects.filter(pk=1)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

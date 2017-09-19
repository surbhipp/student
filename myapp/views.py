# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Team, StudentInfo
from .serializer import StudentSerializer, TeamSerializer, StudentInfoSerializer
from rest_framework.renderers import JSONRenderer
import json
from django.http import HttpResponse
import csv
from django.contrib.auth.models import User


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Roll_No', 'Age', 'Standard'])

    users = Student.objects.all().values_list('Name', 'Roll_No', 'Age', 'Standard')
    for user in users:
        writer.writerow(user)

    return response


class TeamList(APIView):
    def get(self, request):
        Team_info = Team.objects.all()  # to get all of the data
        serializer = TeamSerializer(Team_info, many=True)  # convert it into json
        print 'get method is called'
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print 'POST method is called'
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(APIView):

    def get(self, request):
        Student_update = Student.objects.get(id=2)
        Student_update.Age = 18
        Student_update.save()
         #
         # Create_Student = Student(Name='S9', Age=4, Roll_No=11, Standard='5')
         #
         # Create_Student.save()

        Student_info = Student.objects.all()
        serializer = StudentSerializer(Student_info, many=True)  # convert it into json
        StudentAdditionalInfo = StudentInfo.objects.all()
        serializer1 = StudentInfoSerializer(StudentAdditionalInfo, many=True)
        print 'get method is called'
        Serializer_list = [serializer.data, serializer1.data]
        content = {
            'status': 1,
            'responseCode': status.HTTP_200_OK,
            'data': Serializer_list,
            }
        return Response(content)


    def post(self, request):
        print request.data

        serializer = StudentSerializer(data=request.data)
        # serializer = StudentSerializer(request.data)
        #  serializer2 = StudentInfoSerializer(request.data)

        # serializer1 = StudentInfoSerializer(data=request.data)

        if serializer.is_valid():  #and serializer1.is_valid():
            serializer.save()
            # print "Student Data:", serializer1.data
            # print "Student Info data:", serializer2.data
            # # serializer1.save()
            print 'address:', request.data["Add"]

            print 'POST method is called'
        #     # Serializer_list = [serializer.data, serializer1.data]
        #     # content = {
        #     #     'status': 1,
        #     #     'responseCode': status.HTTP_201_CREATED,
        #     #     'data': Serializer_list,
        #     #         }
        #     # data3 = StudentSerializer.loads(serializer)
        #     # data3.append(StudentInfoSerializer)
        #     # Student.dumps(data3)
            return Response(serializer.data , status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Cricket(APIView):
    def get(self,request):
        team_info = Student.objects.filter(select_team_id=1)
        serializer = StudentSerializer(team_info, many=True)  # convert it into json
        print 'get method is called'
        return Response(serializer.data)


class Football(APIView):
    def get(self,request):
        team_info = Student.objects.filter(select_team_id=2)
        serializer = StudentSerializer(team_info, many=True)  # convert it into json
        print 'get method is called'
        return Response(serializer.data)


class Hockey(APIView):
    def get(self,request):
        team_info = Student.objects.filter(select_team_id=3)
        serializer = StudentSerializer(team_info, many=True)  # convert it into json
        print 'get method is called'
        return Response(serializer.data)


class Recent(APIView):
    def get(self, request):
        team_info = Student.objects.order_by('id').first()
        serializer = StudentSerializer(team_info)  # convert it into json
        print 'get method is called'
        return Response(serializer.data)



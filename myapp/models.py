# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Team(models.Model):
    Team_Name = models.CharField(max_length=10)

    def __str__(self):
        return self.Team_Name


class Student(models.Model):
    Name = models.CharField(max_length=15)
    Standard = models.CharField(max_length=2)
    Age = models.IntegerField(default=15)
    Roll_No = models.IntegerField(default=50)
    #select_team = models.ForeignKey(Team)


    def __str__(self):
        return self.Name


class StudentInfo(models.Model):
    Address = models.CharField(max_length=30)
    MobileNo = models.CharField(max_length=12)

    def __str__(self):
        return self.id










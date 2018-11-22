from django.shortcuts import render
from django.db import DatabaseError, connections
from use_function import namedtuplefetchall, removeExtremum, getListAvg
from datetime import datetime, date
import json
import pandas as pd


def analysis_forum(request):


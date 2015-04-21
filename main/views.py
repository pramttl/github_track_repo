from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import requests

from .models import *
import random

from django.views.decorators.csrf import csrf_exempt


def index(request):
    """
    Select project from dropdown
    """
    pass


def track(request):
    """
    Add a project to track
    """
    pass

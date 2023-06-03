from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse(date.today())


def goodby_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return HttpResponse('Goodby user!')

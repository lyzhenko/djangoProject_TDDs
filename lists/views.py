from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return  HttpResponse('<!DOCTYPE html><title>To-Do List</title></html>')

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def entrypage(request):
    return render(request, "web/entrypage.html")
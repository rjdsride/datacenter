from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator

# from django.http import Http404

from datacenter.models import Cable


def create(request):
    context = {}

    return render(request, "datacenter/create.html", context)

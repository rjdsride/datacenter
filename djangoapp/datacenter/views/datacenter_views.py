from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator

# from django.http import Http404

from datacenter.models import Cable


def index(request):
    cables = Cable.objects.filter(show=True).order_by("-id")

    paginator = Paginator(cables, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "site_title": "Datacenter",
    }

    return render(request, "datacenter/index.html", context)


def cable(request, cable_id):
    # single_cable = Cable.objects.filter(pk=cable_id).first()
    single_cable = get_object_or_404(Cable, pk=cable_id, show=True)

    context = {
        "cable": single_cable,
    }

    return render(request, "datacenter/cable.html", context)


def search(request):
    search_value = request.GET.get("q", "").strip()

    if search_value == "":
        return redirect("datacenter:index")

    cables = (
        Cable.objects.filter(show=True)
        .filter(
            Q(id__icontains=search_value)
            | Q(pontaA__icontains=search_value)
            | Q(pontaB__icontains=search_value),
        )
        .order_by("-id")
    )

    paginator = Paginator(cables, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "site_title": "Search - ",
        "search_value": search_value,
    }

    return render(request, "datacenter/index.html", context)

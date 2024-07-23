import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request,*args, **kwargs):
    qs = PageVisits.objects.all()
    queryset = PageVisits.objects.filter(path=request.path)
    my_title = "my page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count(),
        "total_visit_count": qs.count(),
    }
    path = request.path
    html_template = "home.html" 
    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)
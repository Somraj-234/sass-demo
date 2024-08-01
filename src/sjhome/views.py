import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from visits.models import PageVisits

LOGIN_URL = settings.LOGIN_URL


this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request,*args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    return about_view(request, *args, **kwargs)


def about_view(request,*args, **kwargs):
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

VALID_CODE = "abc123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = False
    if request.method=="POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = True
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})

@login_required(login_url=LOGIN_URL)
def user_only_view(request,*args, **kwargs):
    return render(request, "protected/user-only.html", {})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request,*args, **kwargs):
    return render(request, "protected/user-only.html", {})
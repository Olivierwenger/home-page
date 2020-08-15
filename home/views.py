from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from home.models import LinkEntry


def index(request):
    link_list = LinkEntry.objects.all()
    context = {'link_list': link_list}
    return render(request, 'home/link-list.html', context)
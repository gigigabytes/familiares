from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from .models import Familiar
from django.urls import reverse


class FamiliarListView(View):
     template_name = 'familiares/index.html'

def index(request):
    familiares = Familiar.objects.all()
    context = {'familiares': familiares}
    return render(request, 'familiares/index.html', context)
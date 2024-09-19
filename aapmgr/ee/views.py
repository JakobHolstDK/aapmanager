from django.shortcuts import render

# Create your views here.
from .models import EEDefinition, PipPackage, AnsibleCollection, AnsibleRole, RedhatRepository


def home(request):
    return render(request, 'home.html')

def define_runtime(request):
    return render(request, 'runtime.html')


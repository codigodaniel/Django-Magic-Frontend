from django.shortcuts import render_to_response
from django.template import RequestContext

from catalog.models import Product
from catalog.models import Category

APP_LABEL=Product._meta.app_label

def index(request):
    return render_to_response(APP_LABEL+'/index.html', {}, context_instance=RequestContext(request))
    
def homepage(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

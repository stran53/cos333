from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

def index(request):
	context=RequestContext(request)
	context_dict={'boldmessage': "I am bold font from the context"}
	return render_to_response('example/index.html', context_dict, context)

def about(request):
	context=RequestContext(request)
	return render_to_response('example/about.html', context)

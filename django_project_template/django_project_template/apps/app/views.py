from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response, get_object_or_404



def index(request):

	return HttpResponse('hello django')





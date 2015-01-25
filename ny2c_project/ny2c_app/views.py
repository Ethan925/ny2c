from django.shortcuts import render, render_to_response, RequestContext
from ny2c_app.models import *

# Create your views here.
def home(request):
	pizzas = Pizza.objects.all()
	orders = Order.objects.all()
	context = {"pizzas":pizzas}
	context = {"orders":orders}
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))
# Create your views here.

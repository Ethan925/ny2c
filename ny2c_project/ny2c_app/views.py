from django.shortcuts import render, render_to_response, RequestContext
from ny2c_app.models import *
from django.views.generic import View

# # Create your views here.
# def home(request):
# 	pizzas = Pizza.objects.all()
# 	orders = Order.objects.all()
# 	context = {"pizzas":pizzas}
# 	context = {"orders":orders}
# 	return render_to_response("home.html", locals(), context_instance=RequestContext(request))


class HomeView(View):

	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		# form = NewPizzaForm()
	 	pizzas = Pizza.objects.all()
	 	orders = Order.objects.all()
	 	context = {"pizzas":pizzas}
	 	context = {"orders":orders}
		return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Activities
#def index(request):
    #return HttpResponse("Hello world!")
def house(request):
  #return HttpResponse(template.render())
    #context = {}
    activities = Activities.objects.all()
    template = loader.get_template('house/myfirst.html')
    #context['activities'] = activities
    context = {
        'activities': activities,
    }
    #changed from return render(request, 'house.html', context), also created a house directory inside templates to put myfirst.html in
    return render(request, 'house/myfirst.html', context)

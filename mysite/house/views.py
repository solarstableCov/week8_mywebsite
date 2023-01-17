from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Activities
from django.shortcuts import get_object_or_404, render

def detail(request, activity_id):
    activity = get_object_or_404(Activities, pk=activity_id)
    return render(request, 'house/detail.html', {'activity': activity})

    #return HttpResponse("You're looking at activity %s." % activity_id)
    
    #try:
        #activity = Activities.objects.get(pk=activity_id)
    #except Activities.DoesNotExist:
        #raise Http404("Activity does not exist")
    #return render(request, 'house/detail.html', {'activity': activity})
    
def about(request, activity_id):
    response = "You're looking at the description of activity %s."
    return HttpResponse(response % activity_id)
def category(request, activity_id):
    return HttpResponse("You're categorising activity %s." % activity_id)
#def index(request):
    #return HttpResponse("Hello world!")
def house(request):
  #return HttpResponse(template.render())
    #context = {}
    activities = Activities.objects.all()
    #using shortcut from tutorial03
    #template = loader.get_template('house/myfirst.html')
    #context['activities'] = activities
    context = {
        'activities': activities,
    }
    #changed from return render(request, 'house.html', context), also created a house directory inside templates to put myfirst.html in
    return render(request, 'house/myfirst.html', context)
    #return HttpResponse(template.render(context, request))
    
    
    
    

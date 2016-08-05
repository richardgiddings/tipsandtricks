from django.shortcuts import render_to_response
from .models import Section, Tip, Trick

def index(request):
    """
    All Sections
    """

    section_list = Section.objects.order_by('title')

    return render_to_response("tips/index.html", { 
            "section_list": section_list,
            })

def section(request, section_id):
    """
    Display the tips and tricks within a Section
    """

    # get all tips for this section_id
    tips = Tip.objects.filter(section=section_id).order_by('title')
    
    # get all tricks for each tip
    tricks = Trick.objects.all()

    return render_to_response("tips/section.html", { 
            "tips": tips,
            "tricks": tricks,
            })
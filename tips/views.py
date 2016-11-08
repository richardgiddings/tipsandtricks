from .models import Section, Tip, Trick

from rest_framework import viewsets
from .serializers import SectionSerializer, TipSerializer, TrickSerializer, TipTrickSerializer

class TipTricksList(viewsets.ModelViewSet):
    """
    Get tips and tricks for display.
    """
    serializer_class = TipTrickSerializer

    def get_queryset(self):
        id = self.kwargs['section_id']
        return Tip.objects.filter(section=id)

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sections to be viewed or edited.
    """
    queryset = Section.objects.order_by('title')
    serializer_class = SectionSerializer

class TipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tips to be viewed or edited.
    """
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class TrickViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tricks to be viewed or edited.
    """
    queryset = Trick.objects.all()
    serializer_class = TrickSerializer
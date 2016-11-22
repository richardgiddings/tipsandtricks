from django.core.urlresolvers import reverse
from .models import Section, Tip, Trick
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from collections import OrderedDict

def _create_section(title):
    """
    Create an instance of a Section model
    """
    return Section.objects.create(title=title)

def _create_tip(title, notes, section):
    """
    Create an instance of a Tip model
    """
    return Tip.objects.create(title=title, notes=notes, section=section)

def _create_trick(command, tip):
    """
    Create an instance of a Trick model
    """
    return Trick.objects.create(command=command, tip=tip)

class APITests(APITransactionTestCase):
    """
    Test the Django Rest Framework API.
    """

    reset_sequences = True

    def setUp(self):
        section = _create_section('Section 1')
        tip = _create_tip('Tip 1', 'Some notes', section)
        trick = _create_trick('Trick', tip)

    def test_section_viewset(self):
        """
        Test API for Section retrieval.
        """
        response = self.client.get('/api/sections/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict([
             ('count', 1), 
             ('next', None), 
             ('previous', None), 
             ('results', [OrderedDict([
                            ('id', 1), 
                            ('title', 'Section 1')
                          ])])
        ]))

    def test_tip_viewset(self):
        """
        Test API for Tip retrieval.
        """
        response = self.client.get('/api/tips/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict([
             ('count', 1), 
             ('next', None), 
             ('previous', None), 
             ('results', [OrderedDict([
                            ('id', 1), 
                            ('title', 'Tip 1'),
                            ('notes', 'Some notes'),
                            ('section', 1)
                          ])])
        ]))

    def test_trick_viewset(self):
        """
        Test API for Trick retrieval.
        """
        response = self.client.get('/api/tricks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict([
             ('count', 1), 
             ('next', None), 
             ('previous', None), 
             ('results', [OrderedDict([
                            ('id', 1), 
                            ('command', 'Trick'),
                            ('tip', 1)
                          ])])
        ]))

    def test_tipstricks(self):
        """
        Test that tips and tricks are returned for a section.
        """
        response = self.client.get('/api/tipstricks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict([
             ('count', 1), 
             ('next', None), 
             ('previous', None), 
             ('results', [OrderedDict([
                            ('id', 1), 
                            ('title', 'Tip 1'),
                            ('notes', 'Some notes'),
                            ('section', 1),
                            ('tricks', [OrderedDict([
                                            ('id', 1), 
                                            ('command', 'Trick'),
                                            ('tip', 1)
                                       ])])
                          ])])
        ]))




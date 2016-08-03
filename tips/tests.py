from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Section, Tip, Trick

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

class TipsViewTests(TestCase):

    def test_index_no_sections(self):
        response = self.client.get(reverse('tips:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/index.html')
        self.assertContains(response, 'There are no sections yet.')

    def test_index_with_sections(self):
        _create_section('Section 1')
        _create_section('Section 2')
        response = self.client.get(reverse('tips:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/index.html')
        self.assertQuerysetEqual(response.context['section_list'], 
            ['<Section: Section 2>', '<Section: Section 1>'])

    def test_section_with_no_tips(self):
        s = _create_section('Section 3')
        response = self.client.get(reverse('tips:section', args=(s.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/section.html')
        self.assertContains(response, 'There are no tips yet.')

    def test_section_with_tips_and_tricks(self):
        s4 = _create_section('Section 4')
        s5 = _create_section('Section 5')
        tip1 = _create_tip('Tip 1', 'Some notes', s4)
        tricks = _create_trick('SELECT * FROM section', tip1)
        tip2 = _create_tip('Tip 2', 'Some notes', s5)

        response = self.client.get(reverse('tips:section', args=(s4.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/section.html')
        self.assertQuerysetEqual(response.context['tips'], 
                                                 ['<Tip: Tip 1>'])
        self.assertQuerysetEqual(response.context['tricks'], 
                                                 ['<Trick: SELECT * FROM section>'])

        response = self.client.get(reverse('tips:section', args=(s5.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tips/section.html')
        self.assertQuerysetEqual(response.context['tips'], 
                                                 ['<Tip: Tip 2>'])
        self.assertQuerysetEqual(response.context['tricks'], [])




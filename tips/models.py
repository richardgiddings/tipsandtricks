from django.db import models

class Section(models.Model):

    title = models.CharField(max_length=20,
                                     help_text="Section title")

    def __str__(self):
        return self.title

class Tip(models.Model):
    title = models.CharField(max_length=20,
                             help_text="Tip title")

    notes = models.CharField(max_length=200,
                             help_text="Tip notes")

    section = models.ForeignKey(Section)

    def __str__(self):
        return self.title

class Trick(models.Model):

    command = models.CharField(max_length=50,
                               help_text="Tip command")

    tip = models.ForeignKey(Tip)

    def __str__(self):
        return self.command
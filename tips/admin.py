from django.contrib import admin
from .models import Section, Tip, Trick

admin.site.register(Section)

class TrickInline(admin.StackedInline):
    model = Trick
    extra = 2

class TipAdmin(admin.ModelAdmin):
    inlines = [TrickInline]

admin.site.register(Tip, TipAdmin)

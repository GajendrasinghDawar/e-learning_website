from django import forms
from django.forms.models import inlineformset_factory
from django.forms import Textarea, TextInput

from .models import Course, Module


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Course
        fields = ['subject', 'title', 'slug', 'overview', ]
        widgets = {
            'title': TextInput(attrs={'class': "input "}),

            'slug': TextInput(attrs={'class': "input"}),
            'overview': Textarea(attrs={'class': "textarea"}),
        }


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True, widgets={
                                          'title': TextInput(attrs={'class': "input"}),

                                          'slug': TextInput(attrs={'class': "input"}),
                                          'description': Textarea(attrs={'class': "textarea", 'rows': "4", 'cols': "50"}),
                                      })

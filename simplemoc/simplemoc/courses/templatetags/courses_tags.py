# -*- coding: utf-8 -*-
from django import template
from ..models import Enrollment

register = template.Library()

template.Library.assignment_tag = template.Library.simple_tag

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context

@register.inclusion_tag('courses/templatetags/my_courses_panel.html')
def my_courses_panel(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context
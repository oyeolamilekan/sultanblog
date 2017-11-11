from django import template
from ..forms import feedBackForm

register = template.Library()

@register.inclusion_tag('_forms.html')
def report_form():
	form = feedBackForm()
	return {'form':form}
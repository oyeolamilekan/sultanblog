from django import template
from ..forms import feedBackForm,AskJolaForm

register = template.Library()

@register.inclusion_tag('_forms.html')
def report_form():
	form = feedBackForm()
	return {'form':form}

@register.inclusion_tag('ask_forms.html')
def ask_form():
	form = AskJolaForm()
	return {'form':form}
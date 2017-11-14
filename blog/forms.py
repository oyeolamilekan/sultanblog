from django import forms
from .models import Mentee,AskJola

class feedBackForm(forms.ModelForm):
	class Meta:
		model = Mentee
		fields = ('name','phone_number','email_field')

class AskJolaForm(forms.ModelForm):
	class Meta:
		model = AskJola
		fields = ('name','email_state','body')
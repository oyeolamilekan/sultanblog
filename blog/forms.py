from django import forms
from .models import Mentee

class feedBackForm(forms.ModelForm):
	class Meta:
		model = Mentee
		fields = ('name','phone_number','email_field')
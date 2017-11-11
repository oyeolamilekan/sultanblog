from django import forms
from .models import Feedback

class feedBackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('name','phone_number','email_field')
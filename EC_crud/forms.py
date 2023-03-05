from django import forms
from .models import BMImodel
#from django.forms.widgets import RadioFieldRenderer

Choices =[("male","Male"),("female","Female")]

class BMIform(forms.ModelForm):
	gender=forms.CharField(widget=forms.RadioSelect(choices=Choices))
	class Meta:
		model=BMImodel
		fields=['Fullname','gender','height','weight']


#my_field = forms.ChoiceField(widget=forms.RadioSelect(renderer=forms.RadioFieldRenderer(attrs={'class': 'inline'})), choices=MyModel.MY_CHOICES)
    
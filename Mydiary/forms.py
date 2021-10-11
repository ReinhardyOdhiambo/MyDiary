from django import forms
from .models import NewEntry


class EntryForm(forms.ModelForm):
	class Meta:
		model = NewEntry
		fields = ('Topic','TodaysEntry')
from django import forms
from .models import WorkerType

class WorkerTypeForm(forms.ModelForm):

    class Meta:
        model = WorkerType
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
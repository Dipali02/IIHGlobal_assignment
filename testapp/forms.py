from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_fess(self):
        inputfees=self.cleaned_data['fees']
        if inputfees <5000:
            raise forms.ValidationError('The minimum fee should be 5000')
        return inputfees
    class Meta:
        model=Student
        fields='__all__'

from django import forms
from .models import Assignment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','content','photo','pay_coin','end_at',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','작성합시다.'))
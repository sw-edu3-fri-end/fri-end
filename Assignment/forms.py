from django import forms
from .models import Assignment
from Submission.models import Submission
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title','content','photo','end_at',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','작성합시다.'))

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'content', 'image',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','제출.'))

# forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import SurveyResponse

class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['score', 'comments']
    """    
    def __init__(self, *args, **kwargs):
        super(SurveyResponseForm, self).__init__(*args, **kwargs)
        
        survey_type = self.instance.survey.survey_type.name
        # Set widget attributes based on survey type
        if survey_type == 'CSAT' or survey_type == 'CES':
            self.fields['score'].widget.attrs.update({'min': 0, 'max': 5})
            self.fields['score'].help_text = 'Please enter a score between 0 and 5.'
        elif survey_type == 'NPS':
            self.fields['score'].widget.attrs.update({'min': 0, 'max': 10})
            self.fields['score'].help_text = 'Please enter a score between 0 and 10.'
    """
    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey', None)  # Get the survey instance if provided
        # self.survey = kwargs.pop('survey', None)  # Get the survey instance if provided
        # super(SurveyResponseForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        if survey is not None:
            self.instance.survey = survey  # Assign survey to instance directly
        
        # self.survey = survey

        
        if  survey:
            survey_type = survey.survey_type.name
            # Set widget attributes based on survey type
            if survey_type == 'CSAT' or survey_type == 'CES':
                self.fields['score'].widget.attrs.update({'min': 0, 'max': 5})
                self.fields['score'].help_text = 'Please enter a score between 0 and 5.'
            elif survey_type == 'NPS':
                self.fields['score'].widget.attrs.update({'min': 0, 'max': 10})
                self.fields['score'].help_text = 'Please enter a score between 0 and 10.'
        


    def clean_score(self):
        score = self.cleaned_data.get('score')
        survey = self.instance.survey
        
        # Ensure survey is provided and valid
        if survey:
            #survey_type_name = self.instance.survey.survey_type.name
            survey_type = survey.survey_type.name
            #survey_type_name = self.survey.survey_type.name
            if survey_type in ['CSAT', 'CES'] and not (0 <= score <= 5):
                raise forms.ValidationError("CSAT and CES scores must be between 0 and 5.")
            elif survey_type == 'NPS' and not (0 <= score <= 10):
                raise forms.ValidationError("NPS scores must be between 0 and 10.")
        
        return score
        #return self.cleaned_data['score']
    
    
    """

    def clean_score(self):
        score = self.cleaned_data.get('score')
        if self.survey:  # Use self.survey instead of self.instance.survey
            survey_type = self.survey.survey_type.name
            if survey_type in ['CSAT', 'CES'] and not (0 <= score <= 5):
                raise ValidationError('CSAT and CES scores must be between 0 and 5.')
            elif survey_type == 'NPS' and not (0 <= score <= 10):
                raise ValidationError('NPS scores must be between 0 and 10.')
        return score
    
    def clean_score(self):
        score = self.cleaned_data.get('score')
        # survey_type = self.instance.survey.survey_type.name

        if survey_type == 'CSAT' or survey_type == 'CES':
            if not (0 <= score <= 5):
                raise forms.ValidationError('CSAT and CES scores must be between 0 and 5.')
        elif survey_type == 'NPS':
            if not (0 <= score <= 10):
                raise forms.ValidationError('NPS scores must be between 0 and 10.')

        return score
    """


"""
from django import forms
from .models import SurveyResponse

class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['score', 'comments']
        labels = {
            'score': 'Score (1-10)',
            'comments': 'Comments (optional)',
        }
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'comments': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }


#####
# forms.py

from django import forms
from .models import SurveyResponse

class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['score', 'comments']  # Only include fields the user can modify
"""
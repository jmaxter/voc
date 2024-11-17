from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

class ValueChainStep(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SurveyType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # CSAT, NPS, CES
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Survey(models.Model):
    step = models.ForeignKey(ValueChainStep, on_delete=models.CASCADE, related_name="surveys")
    survey_type = models.ForeignKey(SurveyType, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return f"{self.survey_type} for {self.step}"


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="responses")
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    score = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    """
    def clean(self):
        # Enforce score range based on survey type
        if self.survey.survey_type.name == 'CSAT' or self.survey.survey_type.name == 'CES':
            if not (0 <= self.score <= 5):
                raise ValidationError({'score': 'CSAT and CES scores must be between 0 and 5.'})
        elif self.survey.survey_type.name == 'NPS':
            if not (0 <= self.score <= 10):
                raise ValidationError({'score': 'NPS scores must be between 0 and 10.'})
    """
    def clean(self):
        # Only perform validation if survey is set
        if self.survey:
            survey_type = self.survey.survey_type.name
            """
            if self.survey.survey_type.name in ['CSAT', 'CES'] and not (0 <= self.score <= 5):
                raise ValidationError("CSAT and CES scores must be between 0 and 5.")
            elif self.survey.survey_type.name == 'NPS' and not (0 <= self.score <= 10):
                raise ValidationError("NPS scores must be between 0 and 10.")
            """
            if survey_type in ['CSAT', 'CES'] and not (0 <= self.score <= 5):
                raise ValidationError({'score': 'CSAT and CES scores must be between 0 and 5.'})
            elif survey_type == 'NPS' and not (0 <= self.score <= 10):
                raise ValidationError({'score': 'NPS scores must be between 0 and 10.'})

    def save(self, *args, **kwargs):
        # Call clean() to enforce validation before saving
        self.clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Response by {self.respondent.username} for {self.survey}"

"""
class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="responses")
    respondent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")  # Tied to a logged-in user
    score = models.IntegerField()  # Could use validators for range based on survey type (CSAT, NPS, CES)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.respondent.username} for {self.survey}"
"""

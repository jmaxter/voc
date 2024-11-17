# survey/admin.py

from django.contrib import admin
from .models import ValueChainStep, SurveyType, Survey, SurveyResponse

@admin.register(ValueChainStep)
class ValueChainStepAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SurveyType)
class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey_type', 'step', 'question')
    list_filter = ('survey_type', 'step')
    search_fields = ('question',)

@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('survey', 'respondent', 'score', 'created_at')
    list_filter = ('survey', 'respondent')
    search_fields = ('comments',)
    readonly_fields = ('created_at',)

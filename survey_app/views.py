from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import Survey, SurveyResponse
from .forms import SurveyResponseForm  # This form will be created to handle responses


# View to display surveys for a specific value chain step
@login_required
def survey_list(request, step_id):
    surveys = Survey.objects.filter(step__id=step_id)
    context = {'surveys': surveys, 'step_id': step_id}
    #return render(request, 'survey/survey_list.html', context)
    return render(request, 'survey_list.html', context)

# View to submit a response to a survey
@login_required
def submit_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    step_id = survey.step.id

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST or None, survey=survey)  # Pass survey to form
        if form.is_valid():
            response = form.save(commit=False)
            # response.survey = survey  # Assign survey explicitly
            response.respondent = request.user  # Assign logged-in user
            response.save()
            return redirect('survey_list', step_id=step_id)
    else:
        form = SurveyResponseForm(survey=survey)  # Pass survey to form in GET request

    context = {
        'survey': survey,
        'form': form,
        'step_id': step_id,
    }
    return render(request, 'survey/submit_response.html', context)

"""
@login_required
def submit_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey
            response.respondent = request.user
            response.save()
            return redirect('survey_list', step_id=survey.step.id)
    else:
        form = SurveyResponseForm()

    context = {'survey': survey, 'form': form}
    return render(request, 'submit_response.html', context)
    #return render(request, 'survey/submit_response.html', context)

@login_required
def submit_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    step_id = survey.step.id  # Get the associated step ID for the survey

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey
            response.respondent = request.user
            response.save()
            return redirect('survey_list', step_id=step_id)  # Redirect with step_id
    else:
        form = SurveyResponseForm()

    context = {'survey': survey, 'form': form, 'step_id': step_id}  # Pass step_id to the template
    return render(request, 'survey/submit_response.html', context)
"""
"""
###
@login_required
def submit_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    step_id = survey.step.id

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey  # Ensure survey is assigned
            response.respondent = request.user  # Assign logged-in user
            response.save()
            return redirect('survey_list', step_id=step_id)
    else:
        form = SurveyResponseForm(survey=survey)  # Pass survey to form

    context = {
        'survey': survey,
        'form': form,
        'step_id': step_id,
    }
    return render(request, 'survey/submit_response.html', context)
"""
###
###
"""
@login_required
def submit_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    step_id = survey.step.id  # Assuming each survey is associated with a step

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save(commit=False)
            response.survey = survey  # Set the survey instance
            response.respondent = request.user  # Set the current user as respondent
            response.save()
            return redirect('survey_list', step_id=step_id)
    else:
        form = SurveyResponseForm(survey=survey)

    context = {
        'survey': survey,
        'form': form,
        'step_id': step_id,
    }
    return render(request, 'survey/submit_response.html', context)
"""
###

# View to list responses submitted by the logged-in user
"""
@login_required
def my_responses(request):
    responses = SurveyResponse.objects.filter(respondent=request.user)
    context = {'responses': responses}
    #return render(request, 'survey/my_responses.html', context)
    return render(request, 'my_responses.html', context)
"""
@login_required
def my_responses(request):
    responses = SurveyResponse.objects.filter(respondent=request.user)

    # Determine a default step_id; here we're using the first response's step ID if available
    step_id = responses.first().survey.step.id if responses.exists() else 1  # Fallback to 1 if no responses

    context = {
        'responses': responses,
        'step_id': step_id  # Pass the step_id to the template
    }
    return render(request, 'survey/my_responses.html', context)

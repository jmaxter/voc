"""
from django.urls import path
from . import views2

urlpatterns = [
    path('', views2.index, name='index'),
    path('accounts/login/', views2.login, name='login'),
    path('logout', views2.logout, name='logout'),
    path('register', views2.register, name='register'),
    path('success', views2.success, name='success'),
]
"""

# survey/urls.py

from django.urls import path
from . import views

"""
urlpatterns = [
    path('step/<int:step_id>/surveys/', views.survey_list, name='survey_list'),
    path('survey/<int:survey_id>/respond/', views.submit_response, name='submit_response'),
    path('my-responses/', views.my_responses, name='my_responses'),
]
"""

urlpatterns = [
    path('survey/step/<int:step_id>/surveys/', views.survey_list, name='survey_list'),  # List surveys for a specific step
    path('survey/<int:survey_id>/respond/', views.submit_response, name='submit_response'),  # Submit response for a specific survey
    path('survey/my-responses/', views.my_responses, name='my_responses'),  # View user's responses
]
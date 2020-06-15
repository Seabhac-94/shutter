from django.forms import ModelForm
from .models import Application

class ApplicationForm(ModelForm):
    class Meta():
        model = Application
        fields = ("name", "email", "phone_number", "job_your_applying_for", "years_experience", "work_experience", "about_you")

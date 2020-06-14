from django.db import models

# Create your models here.

class JobOpening(models.Model):
    """
    job opening to that suitable candidates can apply for
    """
    job_title = models.CharField(max_length=100, default='')
    description = models.TextField()
    closing_date = models.DateField()


class Application(models.Model):
    """
    Applicaiton requirements
    """
    name = models.CharField(max_length=50, default='', blank=False)
    email = models.CharField(max_length=100, default='', blank=False)
    phone_number = models.CharField(max_length=15, default='')
    years_experience = models.IntegerField(blank=False)
    work_experience = models.TextField(blank=False)
    about_you = models.TextField(blank=False)

    def __str__(self):
        return self.name


from django.core.mail import send_mail
import os
# os.environ['DJANGO_SETTINGS_MODULE']

send_mail('Django mail','Test mail','abhinavkrjha10@gmail.com',['abhinavkrjha10@gmail.com'],fail_silently = False)


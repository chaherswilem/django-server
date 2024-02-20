from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    return render(request, 'base/home.html')

def download_resume(request):
    # Path to your resume file within the MEDIA_ROOT directory
    resume_path = os.path.join(settings.MEDIA_ROOT, 'pdf', 'ChaherSouilem-Resume.pdf')
    # Open the file in binary mode
    resume_file = open(resume_path, 'rb')
    # Return the file as a response
    return FileResponse(resume_file, as_attachment=True)

def learning_curve(request):
    return render(request, 'learning_curve.html')


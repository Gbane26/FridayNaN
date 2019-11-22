from django.shortcuts import render

# Create your views here.

from .models import EmailSubscriber
from django.utils import timezone
from datetime import timedelta
import random


def home(request):
    for i in range(0, 100):
        EmailSubscriber.objects.create(email=f"user_{i}@email.com", created_at=timezone.now() - timedelta(days=random.randint(0, 100)))
    return render(request, 'index.html')
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Creates superuser using DJANGO_USER and DJANGO_PASSWORD environment variables'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_USER')
        email = os.environ.get('DJANGO_EMAIL')        
        password = os.environ.get('DJANGO_PASSWORD')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Successfully created superuser.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
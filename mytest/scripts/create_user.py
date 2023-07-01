import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest.settings")

from django.contrib.auth.models import User

# When creating a User, use the function create_user(username, email=None, password=None, **extra_fields)
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
user.last_name = "Lennon"
user.save()

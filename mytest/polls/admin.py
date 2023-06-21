from django.contrib import admin

# Register your models here.

# This makes it so that you can edit Questions from the admin page.
from .models import Question

admin.site.register(Question)


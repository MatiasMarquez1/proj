from django.contrib import admin

# Register your models here.

# This makes it so that you can edit Questions from the admin page.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

#admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)


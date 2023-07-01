from django.contrib import admin

# Register your models here.

# This makes it so that you can edit Questions from the admin page.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]

#admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)


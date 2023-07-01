from django.contrib import admin

# Register your models here.

# This makes it so that you can edit Questions from the admin page.
from .models import Question, Choice

# This makes it so that you can create choices inside the Questions admin page
class ChoiceInLine(admin.StackedInLine):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    # The next line divides the fields into fieldsets with a specified title.
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]

admin.site.register(Question, QuestionAdmin)


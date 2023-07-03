from django.contrib import admin
from .models import Question, Choice

# This makes it so that you can create choices inside the Questions admin page
class ChoiceInLine(admin.StackedInline):
    model = Choice
    
class QuestionAdmin(admin.ModelAdmin):
    # The next line divides the fields into fieldsets with a specified title.
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collpase"]}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)

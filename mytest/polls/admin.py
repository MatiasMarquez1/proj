from django.contrib import admin

<<<<<<< HEAD
from .models import Question

# Register your models here.

admin.site.register(Question)
=======
# Register your models here.

# This makes it so that you can edit Questions from the admin page.
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

>>>>>>> new-things

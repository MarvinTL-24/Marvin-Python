from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["Question_text"]}),
        ("Date information", {"fields": ["publish_data"]}),
    ]
    list_display = ["Question_text", "publish_data", "was_recently_published"]




admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

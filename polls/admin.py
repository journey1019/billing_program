from django.contrib import admin
from .models import Question, Choice  # 모델을 import

# StackedInline / TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None,               {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

# 모델을 admin에 등록
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
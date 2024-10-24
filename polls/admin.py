from django.contrib import admin
from .models import Question, Choice  # 모델을 import

# 모델을 admin에 등록
admin.site.register(Question)
admin.site.register(Choice)



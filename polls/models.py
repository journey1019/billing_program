### CSV 파일에서 데이터가 저장될 모델 정의
import datetime

from django.db import models
from django.utils import timezone

# 예시 세팅 데이터 모델 정의 (question_text= 질문내용, pub_date= 발행일)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 현재로 부터 하루 차감한 어제의 시간, 어제 이후에 발생된 데이터 리턴

# 1 : n (question= 선택지에 해당하는 질문(외래키), choice_text= 선택지, votes= 투표수)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
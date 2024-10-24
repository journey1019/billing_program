### CSV 파일 처리 및 cdr 테이블에 데이터를 삽입하는 뷰 정의
from logging import lastResort

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader # template 를 load 해서 response
from django.shortcuts import get_object_or_404, render # 정형화된 작업은 소스코드를 줄이기 위함

from polls.models import Question



## ## templates를 분리하기 전
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

## ## render 사용 전 (loader 사용 x)
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list, # context를 통해서 template에 데이터를 전달(latest_question_list)
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

""" 
VIEW 에서는 request라는 인자를 받고, HttpResponse를 return 함
Client로 부터 request를 받게되면, 이때 request에는 여러가지 정보들이 담겨있을 것이고, 다시 response를 해줌
response를 해주기 전에 VIEW에서는 데이터 추출, 데이터 저장, 파일 다운로드 등 기능을 수행할 것임
"""
## ## get_object_or_404 사용전
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist: # question_id를 전달받고, Question 조회시, Question에 데이터가 없는 경우
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

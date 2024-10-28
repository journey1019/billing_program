### CSV 파일 처리 및 cdr 테이블에 데이터를 삽입하는 뷰 정의
from logging import lastResort

from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader # template 를 load 해서 response
from django.shortcuts import get_object_or_404, render # 정형화된 작업은 소스코드를 줄이기 위함
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question # 해당 템플릿에서 사용할 모델
    template_name = 'polls/results.html' # 사용할 템플릿 이름

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

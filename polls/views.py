from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http.response import Http404

# Create your views here.
def index(request):
    latest_question_text = Question.objects.order_by('publish_date')[:5]
    context = {
        'latest_question_text': latest_question_text,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'q': question   
    }
    return render(request, 'polls/details.html', context)
   

def result(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'q': question
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
    

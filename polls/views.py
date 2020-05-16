from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
# Create your views here.
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse("You are looking at the question %s." %question_id)
def results(request,question_id):
    response="You are looking at the results of the question  %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on the question number %s." %question_id)
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
   # template=loader.get_template('polls/index.html')
    context={'latest_question_list' : latest_question_list}
    return render(request,'polls/index.html',context)
def totalques(request):
    latest_question_list=Question.objects[:5]
    return HttpResponse("The total number of the questions are %s." %len(latest_question_list))

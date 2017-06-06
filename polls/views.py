from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Question,Choice

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request,'polls/index.html',{'question_list':question_list})

def results(request,question_id):
    return HttpResponse("You are looking at results of %s" % question_id)


def votes(request,question_id):
    return HttpResponse("You are looking at votes for the question with id %s" % question_id)

def detail(request,question_id):
    question_detail = get_object_or_404(Question,id=question_id)
    return render(request,'polls/detail.html',{'question_detail':question_detail})

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    question_list = Question.objects.all()
    return render(request,'polls/index.html',{'question_list':question_list})

def results(request,question_id):
    question_list = get_object_or_404(Question, pk= question_id)
    return render(request,'polls/results.html',{'question_list':question_list})


def votes(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question_detail':question,'error_msg':"You didn't enter a choice ",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args = (question_id,)))

def detail(request,question_id):
    question_detail = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question_detail':question_detail})

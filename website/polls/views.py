from django.http import HttpResponse
def index(req):
    return HttpResponse("Hello, world. You're at the polls")
# Create your views here.
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def questions(req,question_id):
    return render(req,'question.html',{'question':Question.objects.get(id=1).question_text.__str__()})
def votes(req):
    id = question_id
    return render(req,'votes.html',{'choice':Question.objects.get(id = )})
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from pollapp.models import Question

def index(request):
    questions = Question.objects.order_by('-date') # menor a mayor default. Incluir el - para invertir

    context = {
        "questions":questions
    }

    return render(request, "index.html", context)

def detail(request, question_id):
    return HttpResponse(f"This is the question number {question_id}")

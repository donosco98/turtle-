from django.shortcuts import render
from . forms import Add_question
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from . models import Question


def question_list(request):
    ques=Question.objects.all()

    return render(request,'questions.html',{'ques':ques},)

def question_details(request,id):
    ques=Question.objects.get(pk=id)
    return render(request,'question_detail.html',{'ques':ques})


def add_question(request):
    form=Add_question(request.POST)
    if request.method=='POST':


        if form.is_valid():
            print("********")
            form.save()




    form=Add_question()

    return render(request,'form.html',{'form':form } ,)

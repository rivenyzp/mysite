from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from problem.models import problem

# Create your views here.
def problem_show(req):
    is_login = req.session.get('is_login',False)
    if is_login == True:
        result = problem.objects.values_list('problem_name')
        return  render(req,'problem_show.html',
                       {
                           'problem_name':result
                       }
                       )
    else:
        return  render(req,'login.html')

def problem_isRight(req):
    is_login = req.session.get('is_login',False)
    if is_login == True:
        problem_name = req.GET['problem_name']
        theProblem = problem.objects.get(problem_name = problem_name)
        flag = req.GET['flag']
        if flag == theProblem.problem_answer:
            return HttpResponse('Accept!')
        else:
            return  HttpResponse('Wrong answer!')
    else:
        return  render(req,'login.html')


def problem_show_one(req):
    is_login = req.session.get('is_login',False)
    if is_login == True:
        problem_name = req.GET['problem_name']
        #print(problem_name)
        theProblem = problem.objects.get(problem_name=problem_name)
        return render(req,'problem_show_one.html',
                      {
                            'problem_name':theProblem.problem_name,
                            'problem_describe':theProblem.problem_describe
                      }
                      )
    else:
        return  render(req,'login.html')

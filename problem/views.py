from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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


def listing(request):
    problem_list = problem.objects.all()  # 获取所有contacts,假设在models.py中已定义了Contacts模型
    paginator = Paginator(problem_list, 3) # 每页25条

    page = request.GET.get('page',1)
    try:
        problems = paginator.page(page) # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        problems = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problem/problem.html', {'problems': problems})
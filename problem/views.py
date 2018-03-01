from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from problem.models import problem
import json

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


# filter_type 过滤的类型
def listing(request,filter_type='A'):
    if filter_type!='A':
        problem_list =problem.objects.filter(problem_type=filter_type)
    else:
        problem_list = problem.objects.all()  # 获取所有contacts,假设在models.py中已定义了Contacts模型


    paginator = Paginator(problem_list, 5) # 每页5条信息

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

# 对题目进行后台校验，查看正确性。
def problem_check(req):
    answer =req.GET.get('flag_answer')
    pid =req.GET.get('id')
    query_object=problem.objects.get(id__exact=pid)
    # 1对 0错
    if answer ==query_object.problem_answer:
        dic={"key":1}
    else:
        dic={"key":0}
    return HttpResponse(json.dumps(dic),content_type='application/json')

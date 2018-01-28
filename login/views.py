from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from user.models import my_User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',max_length=50)


def is_register(req):
    return render(req,'register.html')

def register(req):
    if req.method == 'POST':
        temp = UserForm(req.POST)
        if temp.is_valid():
            username = temp.cleaned_data['username']
            password = temp.cleaned_data['password']

            my_User.objects.create(username = username,password = password)
            return  HttpResponse('register success!')
    else:
        temp = UserForm()
    return render_to_response('register.html',{'temp',temp},context_instance=RequestContext(req))

def login(req):
    return  render(req,'login.html')

def index(req):
    is_login = req.session.get('is_login',False)
    if is_login:
        username = req.session['username']
        return render(req,'index.html',{'username':username})
    else:
        return  render(req,'index.html',{'username':None})

def login_to(req):
    if req.method == 'POST':
        temp = UserForm(req.POST)
        if temp.is_valid():
            username = temp.cleaned_data['username']
            password = temp.cleaned_data['password']
            is_ok = my_User.objects.filter(username__exact = username,password__exact = password)

            if is_ok:
                req.session['is_login'] = True
                req.session['username'] = username
                #response = HttpResponseRedirect('/login/index')
                #response.set_cookie('username',username,3600)
                #return  render(req,'index.html',{'username':username})
                return  index(req)
            else:
                return HttpResponseRedirect('/login/login')
    else:
        temp = UserForm()
        #return HttpResponse('False')
    return render_to_response('login.html', {'temp', temp}, context_instance=RequestContext(req))

def login_out(req):
    if req.session.get('is_login',False) == True:
        del req.session['is_login']
        del req.session['username']
    return index(req)
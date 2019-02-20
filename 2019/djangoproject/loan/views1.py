import random
import time
import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from loan.pizza import get_stores


#pizza查询页面
def pizza(request):
    return render(request, 'pizza.html')

#pizza查询结果页面
def pizza_action(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        re = get_stores(city)
    return render(request,'pizza1.html',{'re':re,'city':city,'total':len(re)})



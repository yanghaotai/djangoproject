from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from loan.loan2 import res
from loan.idcard import idcard_generator,check_true
from loan.jiami import md5
import random
import time
import json


# Create your views here.
# def index(request):
#     return HttpResponse("Hello Django!")

#首页
def index(request):
    return render(request,'index.html')


#贷款主页
def loan(request):
    return render(request, '1.html')

#贷款结果页面
def loan_action(request):
    # print("dsssssssss")
    if request.method == 'POST':
        amount = request.POST.get('amount', '')
        period = request.POST.get('period', '')
        rate = request.POST.get('rate', '')
        rate1 = request.POST.get('rate1', '')
        repayment = request.POST.get('repayment', '')
        date1 = request.POST.get('date1', '')
        date2 = request.POST.get('date2', '')
        # period1 = range(1,int(period)+1)
        print(amount,period,rate,rate1,repayment,date1,date2)
        # print(type(period1))
        # print(date2-date1)
        s = res(amount, period, rate,rate1,repayment)
        re = s[0]
        lx = s[1]
    return render(request,'2.html',{'amount':amount,'period':period,'rate':rate,'rate1':rate1,'repayment':repayment,'date1':date1,'date2':date2,'re':re,'lx':lx})


# s = Loan(1500000,360,0,0.05635,2)
# print(s.date1,s.date2)
# print(s.res())

#身份证主页
def idcard(request):
    return render(request, 'idcard.html')

#随机生成身份证号
def idcard_action(request):
    # print("dsssssssss")
    if request.method == 'POST':
        idcard = idcard_generator()
    return render(request,'idcard.html',{'idcard':idcard})

#检查是否是身份证号码主页
def ifidcard(request):
    return render(request, 'ifidcard.html')

#检查是否是身份证号码结果页
def ifidcard_action(request):
    # print("dsssssssss")
    if request.method == 'POST':
        idcard = request.POST.get('idcard', '')
        ifidcard = check_true(idcard)
    return render(request,'ifidcard.html',{'idcard':idcard,'ifidcard':ifidcard})

#加密主页
def jiami(request):
    return render(request, 'jiami.html')

#加密结果
appid = '100000'
key = '1234567890'
num = random.randint(100,999)
def jiami_action(request):
    if request.method == 'POST':
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(num)
        channelType = request.POST.get('channelType', '')
        transDesc = request.POST.get('transDesc', '')
        businessId = request.POST.get('businessId', '')
        cashierType = request.POST.get('cashierType', '')
        data1 = {"transDesc":transDesc,"businessId":businessId,"channelType":channelType,"cashierType":cashierType}
        print(data1)
        s = appid + '&' + json.dumps(data1) + '&' + timestamp + '&' + key
        sign = md5(s)
        d = {'appId': appid, 'data': json.dumps(data1), 'sign': sign, 'timestamp': timestamp}
        data = json.dumps(d)
    return render(request,'jiami1.html',{'channelType':channelType,'transDesc':transDesc,'businessId':businessId,'cashierType':cashierType,'timestamp':timestamp,'s':s,'sign':sign,'data':data})
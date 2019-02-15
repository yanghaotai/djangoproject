from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from loan.loan2 import res
from loan.idcard import idcard_generator,check_true

# Create your views here.
# def index(request):
#     return HttpResponse("Hello Django!")

def index(request):
    return render(request,'index.html')



def loan(request):
    return render(request, '1.html')


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

def idcard(request):
    return render(request, 'idcard.html')

def idcard_action(request):
    # print("dsssssssss")
    if request.method == 'POST':
        idcard = idcard_generator()
    return render(request,'idcard.html',{'idcard':idcard})

def ifidcard(request):
    return render(request, 'ifidcard.html')

def ifidcard_action(request):
    # print("dsssssssss")
    if request.method == 'POST':
        idcard = request.POST.get('idcard', '')
        ifidcard = check_true(idcard)
    return render(request,'ifidcard.html',{'idcard':idcard,'ifidcard':ifidcard})
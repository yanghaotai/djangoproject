#coding:utf-8

import time
import datetime
from dateutil.relativedelta import relativedelta

'''
'''

def res(amount,period,rate,rate1,repayment):
    # 贷款额为a，月利率为i，年利率为I，日利率为j，还款月数为n
    a = amount
    ssss = []
    zlx = 0
    if rate == '0':
        # 输入年利率
        I = float(rate1)
        i = I / 12
        j = I / 365
    elif rate == '1':
        # 输入月利率
        i = float(rate1)
        I = i * 12
        j = I/365
    elif rate == '2':
        #方案3，输入日利率
        j = float(rate1)
        I = j * 365
        i = I/12

    # print(i * 100, I * 100, j * 100)

    n = int(period)

    # print("借款金额：", a)
    # print("借款期数：", n)


    if repayment == '0':
        # 每月应还本金
        d = int(a) / n
        s = 0
        for m in range(1, n + 1):
            f = (int(a) - d * (m - 1)) * i  # 每月应还利息
            g = d + f
            ssss.append("第%d个月应还利息为%s,应还本金为%s,还款总额(本金+利息)为%s"%(m,round(f,2),round(d,2),round(g,2)))
            s += f
        print("等额本金总利息:", round(s, 2))
        zlx = round(s, 2)
        print(zlx)


    elif repayment == '1':

        print("-----等额本息计算,以" + str(n) + "个月为例-----")
        # 月均还款(本金+利息)
        b = int(a) * i * pow((1 + i), n) / (pow((1 + i), n) - 1)
        # 还款利息总和
        Y = n * int(a) * i * pow((1 + i), n) / (pow((1 + i), n) - 1) - int(a)
        print("等额本息总利息:", round(Y, 2))
        # 第一个月还款利息
        c1 = int(a) * i
        # 剩余利息
        e1 = Y - c1
        # 剩余本金
        a1 = int(a) - (b - c1)
        ssss.append("第1个月应还利息为%s,应还本金为%s,还款总额(本金+利息)为%s" % (round(c1, 2), round(b - c1, 2), round(b, 2)))
        # 第2 - n个月还款利息
        for t in range(2, n + 1):
            ci = (int(a) * i - b) * pow((1 + i), (t - 1)) + b
            bi = b - ci
            ssss.append("第%d个月应还利息为%s,应还本金为%s,还款总额(本金+利息)为%s" % (t, round(ci, 2), round(bi, 2), round(b, 2)))

        zlx = round(Y, 2)
        print(zlx)


    elif repayment == '2':
        print("-----分期还款(等本等息),以" + str(n) + "个月为例-----")
        # 每月应还本金
        dd = int(a) / int(n)
        # 每月应还利息
        df = j * int(a) * (365 / 12)
        for m in range(1,n+1):
            ssss.append("第%d个月应还利息为%s,应还本金为%s,还款总额(本金+利息)为%s"%(m,round(df,2),round(dd,2),round(dd+df,2)))
        # print("分期总利息:", round(df * n, 2))
        zlx = round(df * n, 2)
        print(zlx)

    # return (l, str(day1), ee, round(f, 2), round(ds, 2), round(g, 2), round(sa, 2),round(ss + fs, 2))
    print(ssss)
    return(ssss,zlx)


# s11 = res(1500000,360,'0',0.05635,'2')
# print(s11)





